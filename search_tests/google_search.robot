*** Settings ***
Documentation     A test suite with a single test for valid search.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource1.robot

*** Test Cases ***
Valid Search
    Open Browser                ${SERVER}               chrome
    Maximize Browser Window
    Input Text                  ${INPUTID}              ${SEARCHITEM}
    Click Element               ${SEARCHID}
    sleep                       2
    Click Link                  图片
    Click Element               //div[@id="imgid"][1]/div/ul[@class="imglist clearfix pageNum0"]/li[${PICINDEX}]

    ${titles}                   Get Window Titles
    log to console              ${titles}               DEBUG
    Select Window               title=${titles}[1]
    Capture Page Screenshot     capture.png
    sleep  2

    ${sample}                   set variable            sample.png
    ${capture}                  set variable            capture.png
    ${cmpValue}                 picCompare              ${sample}                   ${capture}
    should be true              ${cmpValue}<20
    should be true              ${cmpValue}>0


    log to console              ${cmpValue}             DEBUG
    [Teardown]                  Close Browser
