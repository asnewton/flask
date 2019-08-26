from flask import Flask
app = Flask(__name__)

@app.route('/')
def indexA():
    return '<h1>Hello Flask</h1>'

@app.route('/learn')
def indexB():
    return '<h3>This is Learning Zone</h3>'

# dynamic routing
@app.route('/myflask/<topic>')
def flask_topic(topic):
    return '<h4>The 10th letter of topic is {} </h4>'.format(topic[10].upper())

@app.route('/latin_topic/<topic>')
def latin_convert(topic):
    if topic[-1] == "y" or topic[-1] == "Y":
        topic1 = topic[:-1] + 'ies'
        return "<h2>Hello {} ! Your Latin name is {} </h2>".format(topic, topic1)
    else:
        topic2 = topic + 'y'
        return "<h2>Hello {} ! Your Latin name is {} </h2>".format(topic, topic2)

    
if __name__ == "__main__":
    app.run(debug=True)

