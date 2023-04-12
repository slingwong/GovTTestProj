from unittest import result

import mariadb
from behave import *
import requests

from Features.test_setup import SessionID, upload_csv_file, create_csv_file
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


#    assert context.response.status_code == 200
@then("System returned status code 400")
def step_impl(context):
    if context.response.status_code != 400:
        raise AssertionError(f"Unexpected status code: {context.response.status_code}")


@step("Database record count should increase by 1")
def step_impl(context):
    initial_count = context.initial_count
    new_count = count_records()
    print("Expected: One record added successfully from " + str(initial_count) + " to " + str(new_count))
    if new_count != initial_count + 1:
        raise AssertionError("Record was not added successfully")


@step("Database record count should not increase")
def step_impl(context):
    initial_count = context.initial_count
    new_count = count_records()
    print("Expected : New count " + str(new_count) + ", and initial count " + str(
        initial_count) + " Record should remained unchanged")
    if new_count != initial_count:
        raise AssertionError("Record was added successfully")


@step('Record "(?P<natid>.+)" already exists should returned')
def step_impl(context, natid):
    response_text = context.response.json()['errorMsg']
    expected_message = "Working Class Hero of natid: " + natid + " already exists!"
    if expected_message not in response_text:
        raise AssertionError("Respond message did not contain record already exists'")
    else:
        print("Record exists in the system")
    return


# User Story 2
@given("I clicked on Upload a csv file button and choose a valid CSV file")
def step_impl(context):
    upload_csv_file()


@when("I clicked on Create button")
def step_impl(context):
    create_csv_file()


@then("CSV file should upload with all the data successfully")
def step_impl(context):
    result = create_csv_file()
    assert result == "Created Successfully!"


