from hashlib import sha256

# -----------------------------
# SHA Generator (unchanged)
# -----------------------------
def SHAGenerator(string, n):
    tmp_sha = str(string)

    if int(n) == 0 or int(n) == 1:
        return sha256(tmp_sha.encode()).hexdigest()

    for _ in range(int(n)):
        tmp_sha = sha256(tmp_sha.encode()).hexdigest()

    return tmp_sha


# -----------------------------
# Detect QR Type
# -----------------------------
def isSecureQr(sample):
    try:
        int(sample)
        return True
    except ValueError:
        return False


# -----------------------------
# Aadhaar Decoder Wrapper
# -----------------------------
def AadhaarQrAuto(data):
    from pyaadhaar_patch.decode import AadhaarSecureQr, AadhaarOldQr

    if isSecureQr(data):
        return AadhaarSecureQr(int(data))
    else:
        return AadhaarOldQr(data)


# -----------------------------
# REMOVE IMAGE PROCESSING ❌
# -----------------------------
# We DO NOT need this anymore because:
# FlutterFlow already gives QR string
#
# ❌ Removed:
# - cv2
# - pyzbar
# - image decoding
#
# -----------------------------
# Instead use this:
# -----------------------------
def qr_text_input(data):
    """
    Directly use QR string from frontend
    """
    return data