import mariadb
from behave import *
import requests
from selenium import webdriver

from Features.test_setup import SessionID, UploadFile
from Features.environment import count_records, create_db_connection

use_step_matcher("re")

url = "http://localhost:9997"


def create_hero(session_id, payload):
    headers = {
        'Content-Type': 'application/json',
        'cookie': 'JSESSIONID=' + session_id
    }
    return requests.request("POST", url + "/api/v1/hero", json=payload, headers=headers)


@given('I have Login with username "(?P<username>.+)" and password "(?P<password>.+)" to retrieve valid JSESSIONID')
def step_impl(context, username, password):
    context.j_session_id = SessionID.get_j_session_id(username, password)


@when("I add a hero with payload details")
@when("I add a duplicate hero with payload details")
def step_impl(context):
    payload = {}
    for row in context.table:
        payload["natid"] = row['natid']
        payload["name"] = row['name']
        payload["gender"] = row['gender']
        payload["birthDate"] = row['birthDate']
        if row["deathDate"] == 'None':
            payload["deathDate"] = None
        else:
            payload["deathDate"] = row['deathDate']
        try:
            payload["salary"] = int(row['salary'])
        except ValueError:
            payload["salary"] = float(row['salary'])
        try:
            payload["taxPaid"] = int(row['taxPaid'])
        except ValueError:
            payload["taxPaid"] = float(row['taxPaid'])
        if row["browniePoints"] == 'None':
            payload["browniePoints"] = None
        else:
            payload["browniePoints"] = int(row['browniePoints'])

    print(f"Processing row with natid {row['natid']}")
    context.initial_count = count_records()
    context.response = create_hero(context.j_session_id, payload)

    print(context.response.content)
    print(context.response.status_code)


@then("System returned status code 200")
def step_impl(context):
    if context.response.status_code != 200:
        raise AssertionError(f"Unexpected status code: {context.response.status_code}")
    return


#    assert context.response.status_code == 200
@then("System returned status code 400")
def step_impl(context):
    if context.response.status_code != 400:
        raise AssertionError(f"Unexpected status code: {context.response.status_code}")
    return


@step("Database record should increase by 1 successfully")
def step_impl(context):
    initial_count = context.initial_count
    new_count = count_records()
    if new_count != initial_count + 1:
        raise AssertionError("Record was not added successfully")
    return


@step("Database record should remain the same")
def step_impl(context):
    initial_count = context.initial_count
    new_count = count_records()
    if new_count != initial_count:
        raise AssertionError("Error, invalid record inserted successfully")
    return


@step("Database record count should not increase")
def step_impl(context):
    initial_count = context.initial_count
    new_count = count_records()
    if new_count != initial_count:
        raise AssertionError("Record was not added successfully")
    return


@given("I clicked on Upload a csv file button and choose a valid CSV file")
def step_impl(context):
    UploadFile.upload_csv_file()
