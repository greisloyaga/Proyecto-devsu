
Feature: Create new user
  Background:
    * def base_url = 'https://petstore.swagger.io/v2/'
    * def requestPayload = read('classpath:payload/user.json')
    * def fakerObj =  new faker()
    * set requestPayload.id = fakerObj.random().nextInt(1000, 9999)
    * set requestPayload.username = 'user' + fakerObj.random().nextInt(1000, 9999)
    * set requestPayload.firstName = fakerObj.name().firstName()
    * set requestPayload.lastName = fakerObj.name().lastName()
    * set requestPayload.email = fakerObj.internet().emailAddress()
    * set requestPayload.password = fakerObj.internet().password()
    * set requestPayload.phone = fakerObj.phoneNumber().phoneNumber()
    * set requestPayload.userStatus = fakerObj.random().nextInt(0, 1)

  Scenario: Create a new user successfully in the pet store.
    Given url base_url
    And path 'user'
    And request requestPayload
    When method post
    Then status 200
    And match $.code == 200
    And match $.message == requestPayload.id.toString()

