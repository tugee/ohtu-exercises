*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kolle
    Set Password  kolle123
    Set Password Confirmation  kolle123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  kolle123
    Set Password Confirmation  kolle123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  xdpp
    Set Password  kolle2
    Set Password Confirmation  kolle2
    Submit Credentials
    Register Should Fail With Message  Password must at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  xdp
    Set Password  kolle2
    Set Password Confirmation  kolle123
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  kolla
    Set Password  kolle123
    Set Password Confirmation  kolle123
    Submit Credentials
    Welcome Page Should Be Open
    Go To Login Page
    Set Username  kolla
    Set Password  kolle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  x
    Set Password  kolle123
    Set Password Confirmation  kolle123
    Submit Credentials
    Go To Login Page
    Set Username  x
    Set Password  kolle123
    Click Button  Login
    Login Page Should Be Open

*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${passwordConf}
    Input Password  password_confirmation  ${passwordConf}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open