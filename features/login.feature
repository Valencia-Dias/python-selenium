Feature: OrangeHrm login

  Scenario: Login to Orangehrm
    Given Launch the browser
    When Open the homepage
    And Enter username Admin and password admin123
    And Click on the login button
    Then User logins successfully



#Data driven
  Scenario Outline: Login to Orangehrm
    Given Launch the browser
    When Open the homepage
    And Enter username <usn> and password <pwd>
    And Click on the login button
    Then User logins successfully
    Examples:
      | usn      | pwd      |
      | Admin    | admin123 |
      | admin123 | Admin    |
      | adminxyz | admin123 |





