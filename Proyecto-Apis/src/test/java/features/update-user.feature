Feature: Update user
  Background:
    * def base_url = 'https://petstore.swagger.io/v2/'
    * def newName = 'Greis'
    * def newEmail = 'gloyagag@gmail.com'


  Scenario: Update the username and email of an existing user in the pet store
    # Call the step to create a user
    Given call read('create-user.feature')
    And url base_url
    And path 'user/' + requestPayload.username
    # Definir el cuerpo de la solicitud con el nuevo nombre y correo electrónico
    And request { username: '#(newName)', email: '#(newEmail)' }
    When method put
    Then status 200

