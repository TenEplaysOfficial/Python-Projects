import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import cv2
from PIL import Image, ImageTk
import os

def generate_qr_code():
    data = qr_entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter data to generate QR Code.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')
    
    # Save the image
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        qr_img.save(save_path)
        messagebox.showinfo("Success", f"QR Code saved as {save_path}")

# Function to decode QR Code from an image
def decode_qr_code():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        img = cv2.imread(file_path)
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(img)

        if data:
            messagebox.showinfo("QR Code Data", f"Decoded Data: {data}")
        else:
            messagebox.showerror("Error", "No QR code found or unable to decode.")

root = tk.Tk()
root.title("QR Code Encoder/Decoder")

qr_label = tk.Label(root, text="Enter data to generate QR Code:", font=('Helvetica', 14))
qr_label.pack(pady=10)

qr_entry = tk.Entry(root, font=('Helvetica', 14), width=40)
qr_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", font=('Helvetica', 14), command=generate_qr_code)
generate_button.pack(pady=10)

decode_button = tk.Button(root, text="Decode QR Code from Image", font=('Helvetica', 14), command=decode_qr_code)
decode_button.pack(pady=20)

root.mainloop()