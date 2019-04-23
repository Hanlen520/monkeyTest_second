@echo off 
color a
title ReleaseAdbPort
echo ======================
echo *** zhangshuiyuan 2019-03-08 ***
echo ***         v1.0.1         ***
echo ======================
echo *****Adapted to Liyu******
echo ---------------------------
echo Checking adb port...
for /F "usebackq tokens=5" %%a in (`"netstat -ano | findstr "5037""`) do (   
if not "%%a" =="0" call :ReleasePort %%a
)
echo ---------------------------
echo adb port has been released!
echo ---------------------------


exit

:ReleasePort
TASKKILL /f /PID %1

exit