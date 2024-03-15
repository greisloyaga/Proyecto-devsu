Feature: Search a modified user

  Scenario: Find a modified user from the pet store.
    # Call the step to create a user
    Given call read('update-user.feature')
    And def requestPayload = response
    And url base_url
    And path 'user/' + newName
    When method get
    Then status 200
    And match $.id == parseInt(requestPayload.message)


