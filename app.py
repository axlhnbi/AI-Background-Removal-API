from flask import Flask, jsonify, request
from lib.rmbg import remove_background
from lib.file import allowed_file, ALlOWED_EXTENSIONS as Extensions, MAX_CONTENT_LENGTH as max_content_length
from PIL import Image

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = max_content_length

@app.route('/api/remove', methods=['POST'])
def post_remove_bg():
    try:
        if 'file' not in request.files:
            return jsonify({ "message": "Invalid request" }), 400
        
        file_image = request.files['file']

        if file_image.filename == '':
            return jsonify({ "message": "Invalid request" }), 400
        
        if not(allowed_file(file_image.filename)):
            return jsonify({ "pesan": f"File extension not allowed. Only accept: {', '.join(Extensions)}" }), 400

        input_image = Image.open(file_image)
        output_image = remove_background(input_image)
        return jsonify({ "message": "success","data": output_image }), 200
    except Exception as e:
        return jsonify({
            "message": e
        }), 500

if __name__ == '__main__':
    app.run(debug=False)