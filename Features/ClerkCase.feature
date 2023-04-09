Feature: Add a hero by Clerk

    Scenario: Post a new hero
        Given I have a valid JSESSIONID
        When I add a hero with valid payload
            | natid   | name  | gender | birthDate              | deathDate | salary | taxPaid | browniePoints |
            | natid-12 | hello | MALE   | 2020-01-01T23:59:59.000 | None      | 10.00  | 1       | 9             |
  #      Then The hero should be added successfully
        Then I will doing a test cleanup
