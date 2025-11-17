*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Page Should Be Open
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  k1
    Set Password Confirmation  k1
    Click Button  Register
    Register Page Should Be Open
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click Button  Register
    Register Page Should Be Open
    Register Should Fail With Message  Password must contain letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Click Button  Register
    Register Page Should Be Open
    Register Should Fail With Message  Password and confirmation do not match

Register With Username That Is Already In Use
    Set Username  tommi
    Set Password  tommi123
    Set Password Confirmation  tommi123
    Click Button  Register
    Register Page Should Be Open
    Register Should Fail With Message  Username already exists

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}


Reset Application Create User And Go To Register Page
    Reset Application
    Create User  tommi  tommi123
    Go To Register Page
