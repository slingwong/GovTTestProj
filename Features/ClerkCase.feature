Feature: Actions by Clerk

    Scenario Outline: US1AC1 Post a new hero
        Given I have Login with username "<username>" and password "<password>" to retrieve valid JSESSIONID
            | username | password |
            | clerk    | clerk    |
        When I add a hero with payload details
            | natid         | name      | gender    | birthDate   | deathDate   | salary    | taxPaid   | browniePoints     |
            | <natid>       | <name>    | <gender>  | <birthDate> | <deathDate> | <salary>  | <taxPaid> | <browniePoints>   |
         Then System returned status code 200

        Examples:
            | natid         | name  | gender | birthDate           | deathDate | salary | taxPaid | browniePoints |
            | natid-12      | hello | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-9999999 | hello | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-0       | hello | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-13      | a     | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-14      | This contains 100 characters for name abcdefghi abcdefghi abcdefghi abcdefghi abcdefghi abcdefghi a | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-15      | Gender Female | FEMALE | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-16      | brownie nullable | FEMALE | 2020-01-01T23:59:59 | None | 10.00 | 1  | None          |


    Scenario Outline: US1AC2 Validate invalid hero
        Given I have Login with username "<username>" and password "<password>" to retrieve valid JSESSIONID
        When I add a hero with payload details
            | natid           | name   | gender    | birthDate    | deathDate   | salary    | taxPaid   | browniePoints     |
            | <natid>         | <name> | <gender>  | <birthDate>  | <deathDate> | <salary>  | <taxPaid> | <browniePoints>   |

        Then System returned status code 400

        Examples:
            | natid           | name            | gender | birthDate           | deathDate | salary | taxPaid | browniePoints |
            | natid-invalid   | Invalid number  | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | invalidnatid-1  | Invalid prefix  | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-10000000  | Out of Range    | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid--1        | Negative number | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-100       |                 | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-101       | 123             | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-102       | This contains 101 characters for name abcdefghi abcdefghi abcdefghi abcdefghi abcdefghi abcdefghi ab | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-103       | Invalid Gender  | MALEFE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-104    | Invalid birthDate  | FEMALE   | 2024-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
            | natid-105    | Salary without decimal  | FEMALE   | 2020-01-01T23:59:59 | None      | 2000   | 1       | 9             |
            | natid-106    | Salary with negative    | FEMALE   | 2020-01-01T23:59:59 | None      | -1     | 1       | 9             |
            | natid-107    | taxPaid without decimal | FEMALE   | 2020-01-01T23:59:59 | None      | 2000   | 1.0     | 9             |
            | natid-108    | taxPaid with negative | FEMALE   | 2020-01-01T23:59:59 | None      | 2000   | -1      | 9             |

   Scenario: US1AC3 Post a duplicate hero
        Given I have Login with username "<username>" and password "<password>" to retrieve valid JSESSIONID
            | username | password |
            | clerk    | clerk    |
       When I add a hero with payload details
            | natid         | name      | gender    | birthDate   | deathDate   | salary    | taxPaid   | browniePoints     |
            | natid-200     | Name new  | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
       Then System returned status code 200
       And Database record count should increase by 1
       When I add a duplicate hero with payload details
            | natid         | name      | gender    | birthDate   | deathDate   | salary    | taxPaid   | browniePoints     |
            | natid-200     | Name duplicate | MALE   | 2020-01-01T23:59:59 | None      | 10.00  | 1       | 9             |
       Then System returned status code 400
       And Database record count should not increase
       And Record "natid-200" already exists should returned

#    Scenario: US2AC1 As a Clerk, I can upload CSV file
#        Given I clicked on Upload a csv file button and choose a valid CSV file
#        When I clicked on Create button
#        Then CSV file should upload with all the data successfully
#
