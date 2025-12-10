@echo off
echo.
echo ===========================================
echo     Victor — Your Private Library Assistant
echo ===========================================
echo.
echo Pulling the Llama 3.2 3B model...
ollama pull llama3.2:3b
echo.
echo Creating Victor from the ModelFile...
ollama create victor -f Victor.ModelFile
echo.
echo ╔══════════════════════════════════════════╗
echo ║    SUCCESS! Victor is ready to go!       ║
echo ║                                          ║
echo ║  Just type the command below and press   ║
echo ║  Enter to start talking to him:          ║
echo ║                                          ║
echo ║       ollama run victor                  ║
echo ╚══════════════════════════════════════════╝
echo.
echo (You can close this window whenever you're done)
echo.

cmd /k