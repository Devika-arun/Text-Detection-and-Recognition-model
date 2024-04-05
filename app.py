from flask import Flask, render_template, request
import easyocr

app = Flask(__name__)

# Load EasyOCR model
reader = easyocr.Reader(['en'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return 'No file uploaded', 400
    
    image_file = request.files['image']
    if image_file.filename == '':
        return 'No selected file', 400

    # Process image and perform OCR
    image = image_file.read()
    result = reader.readtext(image)

    # Extract recognized text
    recognized_text = ' '.join([text[1] for text in result])

    return recognized_text

if __name__ == '__main__':
    app.run(debug=True)