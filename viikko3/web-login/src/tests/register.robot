*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Input Text  username  kille
    Input Password  password  kalle123
    Input Password  password_confirmation  kalle123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Input Text  username  ka
    Input Password  password  kalle123
    Input Password  password_confirmation  kalle123
    Click Button  Register
    Page Should Contain  Invalid username or password

Register With Valid Username And Invalid Password
    Input Text  username  kelle
    Input Password  password  kallekalle
    Input Password  password_confirmation  kallekalle
    Click Button  Register
    Page Should Contain  Invalid username or password

Register With Nonmatching Password And Password Confirmation
    Input Text  username  kulle
    Input Password  password  kalle123
    Input Password  password_confirmation  kalle321
    Click Button  Register
    Page Should Contain  Passwords do not match

Login After Successful Registration
    Go To Login Page
    Set Username  kille
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Set Username  ka
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}