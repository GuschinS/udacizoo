from os import environ
from FlaskExercise import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '13.66.138.105')
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
