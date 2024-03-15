Feature: Update user
  Background:
    * def base_url = 'https://petstore.swagger.io/v2/'
    * def newName = 'Greis7464648767'
    * def newEmail = 'gloyagag@gmail.com'

  Scenario: Update the username and email of an existing user in the pet store
    Given call read('create-user.feature')
    And url base_url
    And path 'user/' + requestPayload.username
    And request { username: '#(newName)', email: '#(newEmail)' }
    * print response
    When method put
    Then status 200

