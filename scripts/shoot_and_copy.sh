#!/bin/bash

# Define the options for taking a screenshot
options=("Fullscreen" "Selected Area" "Active Window" "Delay")

# Create a newline-separated string of options
options_string=$(printf "%s\n" "${options[@]}")

# Use Rofi to display the options and get user input
selected_option=$(echo -e "$options_string" | rofi -dmenu -p "Select Screenshot Type:")

# Function to take a screenshot and save it to the clipboard using xclip
take_screenshot() {
    screenshot_file=~/pictures/screenshots/$(date +%Y%m%d%H%M%S).png
    case "$1" in
        "Fullscreen")
            maim "$screenshot_file"
            ;;
        "Selected Area")
            maim -s "$screenshot_file"
            ;;
        "Active Window")
            maim -i "$(xdotool getactivewindow)" "$screenshot_file"
            ;;
        "Delay")
            delay_time=$(rofi -dmenu -p "Enter Delay in Seconds:")
            sleep "$delay_time"
            maim "$screenshot_file"
            ;;
        *)
            echo "Invalid option"
            ;;
    esac

    # Save the screenshot to the clipboard using xclip
    xclip -selection clipboard -t image/png -i "$screenshot_file"
}

# Call the function with the selected option
take_screenshot "$selected_option"

exit 0
