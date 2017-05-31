from flask import Flask, render_template
import random

app= Flask(__name__)

# List of cat images

images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-07/11/11/enhanced/webdr04/anigif_enhanced-buzz-20968-1405091003-30.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-07/11/10/enhanced/webdr04/anigif_enhanced-buzz-23337-1405089854-4.gif"


]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
