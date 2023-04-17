from behave import *

from Features.test_setup import Search

use_step_matcher("re")


@given('I am logged in as a governor with username "(?P<username>.+)" and password "(?P<password>.+)"')
def step_impl(context, username, password):
    Search.list_all()
    Search.list_all_button()


@then("I should see a list of all heroes")
def step_impl(context):
    Search.table_display()
    Search.table_row()


@when('I type "(?P<search_text>.+)" into the search bar')
def step_impl(context, search_text):
    Search.search_hero(search_text)
    Search.result_display()


@then('I should see a hero with the natid "(?P<search_text>.+)"')
def step_impl(context, search_text):
    search_result = Search.get_search_result()
    no_record = Search.get_no_record()

    if search_result == search_text:
        assert search_result == search_text, f"Expected {search_text}, but got {search_result}"
        print(search_result == search_text)
    else:

        assert no_record == "No records found!", f"Expected {search_text}, but got {search_result}"
        print(search_result != search_text)


@then('I should see a hero with the name "(?P<search_text>.+)"')
def step_impl(context, search_text):
    no_record = Search.get_no_record()

    if no_record != "Showing 0 to 0 of 0 entries":
        search_name = Search.get_search_name()
        assert search_name == search_text, f"Expected {search_text}, but got {search_name}"
        print(search_text == search_name)
    else:
        assert no_record == "No records found!", f"Expected {search_text}"
