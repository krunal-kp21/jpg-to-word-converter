import tkinter as tk
from tkinter import filedialog
from PIL import Image

def upload_and_convert_to_pdf():
    # Open file dialog to select JPG file
    img_file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg")])
    
    if img_file:
        # Open the image file
        img = Image.open(img_file)
        
        # Convert to RGB mode if the image is in palette mode (like PNGs)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Prompt the user to select where to save the PDF file
        pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                filetypes=[("PDF files", "*.pdf")],
                                                title="Save as PDF")
        
        if pdf_file:  # Only proceed if the user provided a filename
            # Save the image as a PDF
            img.save(pdf_file, "PDF", resolution=100.0)
            print(f"Conversion complete. File saved as {pdf_file}")

# Set up Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Run the upload and convert function
upload_and_convert_to_pdf()
