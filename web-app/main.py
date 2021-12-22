from app import app
import os
import socket



if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
#    app.run()
#    app.run(host="localhost", port=os.environ.get('PORT'), debug=True)#
    app.run(host=local_ip, port=os.environ.get('PORT'), debug=True)
#    app.run(host="0.0.0.0", port=os.environ.get('PORT'), debug=True)
#    app.run(host="192.168.1.7", port=os.environ.get('PORT'), debug=True)
#    app.run(host="0.0.0.0", port=os.environ.get('PORT'), debug=True)
#    app.run(host="localhost", port=5000, debug=True)