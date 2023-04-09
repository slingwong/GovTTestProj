import sys

from behave import *
from datetime import datetime

import mariadb
import requests
from test_setup import SessionID

use_step_matcher("re")

url = "http://localhost:9997"


@Then("I will doing a test cleanup")
def step_impl(context):
    print("performing teardown")
    try:
        conn = mariadb.connect(
            user="user",
            password="userpassword",
            host="127.0.0.1",
            port=3306,
            database='testdb'
        )
    except mariadb.Error as e:
        print("error connecting to mariadb")
        print(e)
        sys.exit(1)

    cur = conn.cursor()

    cur.execute("DELETE FROM working_class_heroes WHERE natid = 'natid-12'")
    conn.commit()
    conn.close()


def create_hero(session_id, payload):
    headers = {
        'Content-Type': 'application/json',
        'cookie': 'JSESSIONID=' + session_id
    }
    return requests.request("POST", url + "/api/v1/hero", json=payload, headers=headers)


@given("I have a valid JSESSIONID")
def step_impl(context):
    context.j_session_id = SessionID.get_j_session_id("clerk", "clerk")


@when("I add a hero with valid payload")
def step_impl(context):
    payload = {}
    for row in context.table:
        payload["natid"] = row['natid']
        payload["name"] = row['name']
        payload["gender"] = row['gender']
        payload["birthDate"] = datetime.fromisoformat(row['birthDate']).isoformat()
        payload["deathDate"] = row['deathDate']
        payload["salary"] = float(row['salary'])
        payload["taxPaid"] = int(row['taxPaid'])
        payload["browniePoints"] = int(row['browniePoints'])

    context.response = create_hero(context.j_session_id, payload)


@then("The hero should be added successfully")
def step_impl(context):
    assert context.response.status_code == 201
    print(context.response.content)
    print(context.response.status_code)
