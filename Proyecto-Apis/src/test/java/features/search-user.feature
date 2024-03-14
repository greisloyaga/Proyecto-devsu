Feature: Search user
  Scenario: Find the user in the pet store
    # Call the step to create a user
    Given call read('create-user.feature')

    #Find user
    Given url base_url
    And path 'user/' + requestPayload.username
    When method get
    Then status 200

