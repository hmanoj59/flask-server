from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image part', 400
    file = request.files['image']
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"photo_{timestamp}.jpg"
    file.save(f"./{filename}")
    return 'Image saved!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

