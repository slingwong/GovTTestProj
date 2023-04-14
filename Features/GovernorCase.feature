@feature
Feature: Search Hero
  As the governor, I can search Hero in different ways

  Scenario: US4AC1 List all heroes
    Given I am logged in as a governor with username "gov" and password "gov"
    Then I should see a list of all heroes

  Scenario Outline: US4AC2 Search hero by natid
    Given I am logged in as a governor with username "gov" and password "gov"
    When I type "<search_text>" into the search bar
    And I click on the Search button
    Then I should see a hero with the natid "<search_text>"

    Examples:
      |search_text  |
      |natid-1|
      |not found|

  Scenario Outline: US4AC3 Search hero by name
    Given I am logged in as a governor with username "gov" and password "gov"
    When I type "<search_text>" into the search bar
    And I click on the Search button
    Then I should see a hero with the name "<search_text>"

    Examples:
      |search_text           |
      |Mrs. Martin Champlin  |
      |hello                 |

