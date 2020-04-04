*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary
Library           Screenshot
Library           ../util/picCheck.py

*** Variables ***
${SERVER}         https://www.baidu.com
${BROWSER}        Chrome
${DELAY}          0
${PICINDEX}       3
${SEARCHITEM}     ss
${INPUTID}        kw
${SEARCHID}       su
${SAMPLE}         sample.png
${CAPTURE}        capture.png
