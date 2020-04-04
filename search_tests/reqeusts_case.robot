*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Library           RequestsLibrary

*** Test Cases ***
Get Requests
    create session  github   https://www.baidu.com
    Log     hehe    DEBUG
    ${resp}=        get request     github  /
    log to console   ${resp.text}     DEBUG
    should be equal as strings      ${resp.status_code}     200
