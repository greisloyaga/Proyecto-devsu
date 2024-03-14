Feature: Delete user

  Scenario: Successfully delete user in pet store
    # Call the step to create a user
    Given call read('create-user.feature')

    # Delete the pet from the store
    Given url base_url
    And path 'user/' + requestPayload.username
    When method delete
    Then status 200