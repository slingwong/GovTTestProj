
Feature: Generate Tax Relief Egress File from UI
  As a Book Keeper, I should be able to generate Tax Relief Egress File from UI

  Scenario: Generate Tax Relief Egress File
    Given I am logged in as a Book Keeper with username "bk" and password "bk"
    When I click the Generate Tax Relief File button
    Then the tax relief egress file should be generated
