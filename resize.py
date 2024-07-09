import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from PIL import Image, ImageSequence

def resize_gif(input_path, output_path, size):
    with Image.open(input_path) as img:
        # Get the number of frames in the GIF
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

        # Resize frames
        resized_frames = [frame.resize(size, Image.ANTIALIAS) for frame in frames]

        # Save the resized frames as a new GIF
        resized_frames[0].save(
            output_path,
            save_all=True,
            append_images=resized_frames[1:],
            duration=img.info['duration'],
            loop=img.info['loop']
        )

def select_and_resize_gif():
    # Select the input GIF file
    input_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    if not input_path:
        return

    # Get the desired output path
    output_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    if not output_path:
        return

    # Ask the user for the new size
    width = simpledialog.askinteger("Input", "New width:", minvalue=1)
    height = simpledialog.askinteger("Input", "New height:", minvalue=1)
    if not width or not height:
        return

    # Resize the GIF
    new_size = (width, height)
    resize_gif(input_path, output_path, new_size)
    print(f"Resized GIF saved to {output_path}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    select_and_resize_gif()