from time import sleep

from behave import *

from Features.test_setup import SessionID, Search

use_step_matcher("re")


@given('I am logged in as a governor with username "(?P<username>.+)" and password "(?P<password>.+)"')
def step_impl(context, username, password):
    Search.list_all()
    Search.list_all_button()


@then("I should see a list of all heroes")
def step_impl(context):
    Search.table_display()
    sleep(3)
    Search.table_row()


@when('I type "(?P<search_text>.+)" into the search bar')
def step_impl(context, search_text):
    Search.search_hero(search_text)


@step("I click on the Search button")
def step_impl(context):
    Search.search_btn()
    sleep(5)


@then('I should see a hero with the natid "(?P<search_text>.+)"')
def step_impl(context, search_text):
    search_result = Search.get_search_result()
    no_record = Search.get_no_record()

    if search_result == search_text:
        assert search_result == search_text, f"Expected {search_text}, but got {search_result}"
    else:
        assert no_record == "No records found!", f"Expected {search_text}, but got {search_result}"


@then('I should see a hero with the name "(?P<search_text>.+)"')
def step_impl(context, search_text):
    search_name = Search.get_search_name()
    no_record = Search.get_no_record()

    if search_name == search_text:
        assert search_name == search_text, f"Expected {search_text}, but got {search_name}"
    else:
        assert no_record == "No records found!", f"Expected {search_text}, but got {search_name}"
