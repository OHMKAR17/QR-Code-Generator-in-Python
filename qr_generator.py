
import qrcode
import os

def generate_qr(data, filename):
    if not data.strip():
        print("Error: Text or URL cannot be empty.")
        return

    if not filename.lower().endswith(".png"):
        filename += ".png"

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        image.save(filename)

        print("\nQR code generated successfully!")
        print(f"Saved as: {os.path.abspath(filename)}")

    except (OSError, ValueError) as error:
        print(f"Could not generate QR code: {error}")


print("==============================")
print("       QR CODE GENERATOR")
print("==============================")

content = input("Enter text or a URL: ").strip()
filename = input("Enter output filename (e.g. my_qr.png): ").strip()

if filename:
    generate_qr(content, filename)
else:
    print("Error: Please enter a filename.")
