from app import app
import os


if __name__ == "__main__":
#    app.run()
#    app.run(host="localhost", port=os.environ.get('PORT'), debug=True)
    app.run(host="0.0.0.0", port=os.environ.get('PORT'), debug=True)
#    app.run(host="0.0.0.0", port=os.environ.get('PORT'), debug=True)
#    app.run(host="localhost", port=5000, debug=True)