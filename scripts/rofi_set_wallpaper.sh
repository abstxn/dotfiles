#!/bin/bash

# Folder where the images are stored
IMAGE_DIR="/home/abstxn/Syncthing/Pictures/Wallpapers"

# Use rofi to select an image
SELECTED_IMAGE=$(find "$IMAGE_DIR" -type f \( -iname \*.jpg -o -iname \*.png -o -iname \*.jpeg \) | rofi -dmenu -i -p "Select an image:")

# Check if the user selected an image
if [ -n "$SELECTED_IMAGE" ]; then
    # Set the selected image as the wallpaper using feh
    feh --bg-scale "$SELECTED_IMAGE"
else
    echo "No image selected."
fi

