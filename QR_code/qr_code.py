import qrcode

def generate_qr_code(website_link, box_size=5, border=5, fill_color='black', back_color='white', file_name='qr_code.png'):
    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(website_link)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(file_name)
    print(f"QR code generated for '{website_link}' and saved as '{file_name}'")

def main():
    website_link = input("Enter the website link: ")
    box_size = int(input("Enter the box size (default is 5): ") or 5)
    border = int(input("Enter the border size (default is 5): ") or 5)
    fill_color = input("Enter the fill color (default is 'black'): ") or 'black'
    back_color = input("Enter the background color (default is 'white'): ") or 'white'
    file_name = input("Enter the file name to save the QR code (default is 'qr_code.png'): ") or 'qr_code.png'

    generate_qr_code(website_link, box_size, border, fill_color, back_color, file_name)

if __name__ == "__main__":
    main()
