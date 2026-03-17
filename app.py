from flask import Flask, request, jsonify
from pyaadhaar_patch.decode import AadhaarSecureQr
from pyaadhaar_patch.utils import isSecureQr

app = Flask(__name__)

@app.route('/')
def home():
    return "Aadhaar QR API Running"

@app.route('/decode', methods=['POST'])
def decode_qr():
    try:
        qrData = request.json.get('qr')

        if not qrData:
            return jsonify({"error": "No QR data"}), 400

        if isSecureQr(qrData):
            secure_qr = AadhaarSecureQr(int(qrData))
            data = secure_qr.decodeddata()
            return jsonify(data)

        return jsonify({"error": "Not a secure Aadhaar QR"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()