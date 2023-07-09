Feature: Usage of background

  #The common steps before any specific step are written in the background section.
  # These steps will be executed before every scenario.

  Background: Common steps
    Given Launch the browser
    When Open the homepage
    And Enter username Admin and password admin123
    And Click on the login button

  Scenario: Login to Orangehrm
    Then User logins successfully

  Scenario: Search for a user
    When Navigate to the search page
    Then Search page should be displayed

  Scenario: Search for an advanced user
    When Navigate to the advanced search page
    Then Advanced search page should be displayed