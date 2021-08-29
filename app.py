from flask import Flask, request, render_template
import backend_code
import conect_to_db
import os


'''allocated flask object'''
app = Flask(__name__)
'''allocated object to use the backend code'''
backend = backend_code.backend()

@app.route('/')
def load():
    """loud the form to fill the properties"""
    conect_to_db.sql_create_table()
    return render_template('home.html')

@app.route('/replace-link/', methods=['POST', 'GET'])
def replace():
    """active the function- rename_file when the user submit the properties"""
    if request.method == 'POST':
        oldName = request.form['oldName']
        newName = request.form['newName']
        path = request.form['path']
        backend.renameFile(path, oldName, newName)
        return render_template('success.html')
    return render_template('home.html')

@app.route("/cancel-last-replace/", methods=['POST', 'GET'])
def cancel_last_replace():
    """active the function- cancel_last_action when the user click on the button"""
    if request.method == 'POST':
        backend.cancel_last_action()
        return render_template('home.html')
    return render_template('success.html')

def run_application():
    """function that active the debugger and run the flask application"""
    port = int(os.environ.get("PORT", 5000))
    app.debug= True
    app.run(host="0.0.0.0", port=port)



if __name__ == '__main__':
    run_application()
