from flask import Flask, render_template, request, send_file
from create_email import process
import os
from event_config import *
from config import *
from send_email import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        download_file = request.form.get('download')
        send_email = request.form.get('sendEmail')

        if not os.path.exists('uploaded_files'):
            os.makedirs('uploaded_files')

        if not os.path.exists('generated_emails'):
            os.makedirs('generated_emails')

        if file:
            file.save(f"./uploaded_files/{file.filename}")
            processed_file = process(f"./uploaded_files/{file.filename}")

            if download_file:
                return send_file(processed_file, as_attachment=True)
            
            if send_email:
                send_email(processed_file)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
