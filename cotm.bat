:: Main launcher script
:: Type 'cotm -h' for help
@echo off

setlocal enabledelayedexpansion

if "%~1"=="-h"      goto help
if "%~1"=="--help"  goto help
if "%~1"=="init"    goto init
if "%~1"=="server"  goto start_server
if "%~1"=="python"  goto raw_python

:help
    echo Case of the Mondays launcher
    echo Usage: cotm command [options..] 
    echo. 
    echo Commands:
    echo   init     Initialize workspace
    echo   start    Start server
    exit /b 0

:init
    if not exist .venv (
        echo Creating virtual environment
        python -m venv .venv || exit /b %ERRORLEVEL%
    )

    echo Installing python packages
    call .venv\Scripts\activate
    pip install -r requirements.txt || exit /b %ERRORLEVEL%
    
    echo All good
    exit /b 0

:start_server
    set args=%*
    set "args=!args:server=!"
    call .venv\Scripts\activate
    python server/__main__.py %args% || exit /b %ERRORLEVEL%
    exit /b 0

:raw_python
    set args=%*
    set "args=!args:python=!"
    
    call .venv\Scripts\activate
    python %args% || exit /b %ERRORLEVEL%
    exit /b 0
