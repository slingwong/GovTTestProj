from behave import *

from Features.test_setup import TaxRelief

use_step_matcher("re")


@given('I am logged in as a Book Keeper with username "(?P<username>.+)" and password "(?P<password>.+)"')
def step_impl(context, username, password):
    TaxRelief.generate_tax()


@when("I click the Generate Tax Relief File button")
def step_impl(context):
    TaxRelief.tax_generate_button()


@then("the tax relief egress file should be generated")
def step_impl(context, filename):
    assert filename == 'taxrelief.txt'
