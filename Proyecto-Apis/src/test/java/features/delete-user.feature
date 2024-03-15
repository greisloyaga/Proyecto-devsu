Feature: Delete user

  Scenario: Successfully delete user in pet store

    Given call read('create-user.feature')
    And url base_url
    And path 'user/' + requestPayload.username
    When method delete
    Then status 200
    And match $.message == requestPayload.username.toString()