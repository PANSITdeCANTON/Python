import qrcode

inputQR = input("Input Website Link: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size= 16,
    border= 4,
)

qr.add_data(inputQR)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color = "white")
# img.save("url_qr_code.png")

img.show()

print(qr.data_list)