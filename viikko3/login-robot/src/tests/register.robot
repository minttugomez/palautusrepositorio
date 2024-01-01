*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Invalid username or password

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle2  kalle123
    Output Should Contain  Invalid username or password

Register With Valid Username And Too Short Password
    Input Credentials  kille  ka123
    Output Should Contain  Invalid username or password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kille  kallekille
    Output Should Contain  Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Input New Command