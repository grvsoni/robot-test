*** Settings ***
Documentation     Test suite for Calculator application
Library           CalculatorLibrary.py

*** Test Cases ***
Test Addition
    [Documentation]    Test the add method of Calculator
    [Tags]    addition
    ${result}=    Add Numbers    5    3
    Should Be Equal As Numbers    ${result}    8
    ${result}=    Add Numbers    -2    2
    Should Be Equal As Numbers    ${result}    0
    ${result}=    Add Numbers    10.5    4.5
    Should Be Equal As Numbers    ${result}    15.0

Test Subtraction
    [Documentation]    Test the subtract method of Calculator
    [Tags]    subtraction
    ${result}=    Subtract Numbers    10    3
    Should Be Equal As Numbers    ${result}    7
    ${result}=    Subtract Numbers    5    10
    Should Be Equal As Numbers    ${result}    -5
    ${result}=    Subtract Numbers    0    0
    Should Be Equal As Numbers    ${result}    0

Test Multiplication
    [Documentation]    Test the multiply method of Calculator
    [Tags]    multiplication
    ${result}=    Multiply Numbers    4    5
    Should Be Equal As Numbers    ${result}    20
    ${result}=    Multiply Numbers    -3    3
    Should Be Equal As Numbers    ${result}    -9
    ${result}=    Multiply Numbers    2.5    4
    Should Be Equal As Numbers    ${result}    10.0

Test Division
    [Documentation]    Test the divide method of Calculator including division by zero
    [Tags]    division
    ${result}=    Divide Numbers    10    2
    Should Be Equal As Numbers    ${result}    5
    ${result}=    Divide Numbers    15    3
    Should Be Equal As Numbers    ${result}    5
    ${result}=    Divide Numbers    7    2
    Should Be Equal As Numbers    ${result}    3.5
    Run Keyword And Expect Error    ValueError: Cannot divide by zero    Divide Numbers    10    0
