from flask import Flask, send_from_directory, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/frames/<filename>')
def frame(filename):
    return send_from_directory('frames', filename, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)
