import os

def restart():
    # 执行 pip3 install 命令
    os.system('kill -9 $(lsof -t -i:8008)')

    # os.system('pip3 install --upgrade pandora-chatgpt')
    
    # 执行 python3 auto_pool_token.py 命令
    os.system('python3 /app/ChatGPT-3.5-AccessToken-Web/auto_pool_token.py')
    # os.system('cd /app/pandora')
    # 执行 yarn pandora -s -t tokens.txt &命令
    # os.system('nohup pandora -s 0.0.0.0:8008 -t token.txt > output.log 2>&1 &')
    
    print('Commands executed successfully!')

if __name__ == '__main__':
    restart()