import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("https://soundcloud.com/just_a_phase")


qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')

img.save('just_a_phase_soundcloud_qr.png')
img.show()