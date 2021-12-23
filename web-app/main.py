from app import app
import os
import socket


if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    app.run(host=local_ip, port=os.environ.get('PORT'), debug=True)
    # app.run(host="localhost", port=5000, debug=True)