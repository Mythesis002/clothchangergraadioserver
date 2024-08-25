from flask import Flask, request, jsonify
from flask_cors import CORS
import cloudinary
import cloudinary.uploader
import cloudinary.api

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up Cloudinary credentials
cloudinary.config(
    cloud_name="dkr5qwdjd",
    api_key="797349366477678",
    api_secret="9HUrfG_i566NzrCZUVxKyCHTG9U"
)

@app.route('/uploadclodiver', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(file, folder="Mythesis_images")
        if 'secure_url' in upload_result:
            image_url = upload_result['secure_url']
            
            print("Uploaded Image URL:", image_url)
            
            # Return the uploaded image URL
            return jsonify({'uploadedimage': image_url}), 200
        else:
            return jsonify({'error': 'Failed to upload image to Cloudinary'}), 500
    except Exception as e:
        print(f"Exception occurred: {e}")  # Print exception for debugging
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
