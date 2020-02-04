@echo off
pushd %~dp0

set APP_DIR=..\bin
set APP_XML=application_dev_live.xml
set FLEX_SDK=..\..\libs\ascsdk.29
set SCREEN_SIZE=iPad


:desktop-run
echo.
echo Starting AIR Debug Launcher with screen size '%SCREEN_SIZE%'
echo.

%FLEX_SDK%\bin\adl -extdir ..\lib\air -screensize %SCREEN_SIZE% "%APP_XML%" "%APP_DIR%" -- %1%

popd
if errorlevel 1 goto error
goto end

:error
pause
