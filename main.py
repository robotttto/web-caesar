from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config ['DBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-seriv;
                boreder-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>

    <body>
        <form method="post">
            <div>
                <label for="rot"> Rotate by:</label>
                <input id="rot" type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea id="text" type="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>

    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rots = int(request.form['rot'])
    msg = request.form['text']

    
    message = rotate_string(msg, rots)
    return '<h1>message</h1>'

app.run()

