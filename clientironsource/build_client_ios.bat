echo "pre build"
call pre-build.bat
IF ERRORLEVEL 1 @goto ERROR
echo "build"

fdbuild.exe -notrace -verbosegetoptions -nopostbuild -noprebuild -compiler ..\libs\ascsdk.29\bin client-air-ios.as3proj
IF ERRORLEVEL 1 @goto ERROR
echo "post build"
call post-build.bat
IF ERRORLEVEL 1 @goto ERROR

goto DONE

:ERROR
echo "error..."
pause
exit /B 1

:DONE
pause