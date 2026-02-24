@echo off
echo Syncing changes to GitHub...
git add .
git commit -m "Auto-sync: %date% %time%"
git push origin main
echo.
echo Done! Your changes are now on GitHub.
pause
