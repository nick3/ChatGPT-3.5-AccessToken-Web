python /app/ChatGPT-3.5-AccessToken-Web/autorestart.py
cd /app/pandora
nohup pandora -s 0.0.0.0:8008 --tokens_file /config/tokens.txt > output.log 2>&1 &