#!/bin/bash

# Define the options for taking a screenshot
options=("Fullscreen" "Selected Area" "Active Window" "Delay")

# Create a newline-separated string of options
options_string=$(printf "%s\n" "${options[@]}")

# Use Rofi to display the options and get user input
selected_option=$(echo -e "$options_string" | rofi -dmenu -p "Select Screenshot Type:")

case "$selected_option" in
    "Fullscreen")
        maim ~/pictures/screenshots/$(date +%Y%m%d%H%M%S).png
        ;;
    "Selected Area")
        maim -s ~/pictures/screenshots/$(date +%Y%m%d%H%M%S).png
        ;;
    "Active Window")
        maim -i $(xdotool getactivewindow) ~/pictures/screenshots/$(date +%Y%m%d%H%M%S).png
        ;;
    "Delay")
        delay_time=$(rofi -dmenu -p "Enter Delay in Seconds:")
        sleep "$delay_time"
        maim ~/pictures/screenshots/$(date +%Y%m%d%H%M%S).png
        ;;
    *)
        echo "Invalid option"
        ;;
esac

exit 0

