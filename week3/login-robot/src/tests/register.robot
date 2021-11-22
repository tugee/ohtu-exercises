*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  valid  password123

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  password123
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Input Credentials  aa  password123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  aaa  pass2
    Output Should Contain  Password must at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  aaa  password
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  password123
    Input New Command