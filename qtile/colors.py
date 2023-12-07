colors = []
cache='/home/abstxn/.cache/wal/colors'
with open(cache, 'r') as file:
    for i in range(8):
        colors.append(file.readline().strip())

def to_lux(hx:str) -> float:
    '''
    hx: Some hex color like '#456789'
    returns: Single float value representing its overall brightness
    '''

    hx = hx[1:] # remove '#' from string

    rgb = map(lambda x: int(x, 16), (hx[0:2], hx[2:4], hx[4:6]))
    lux = sum(rgb)

    return lux

# Sort based on brightness
colors = sorted(colors, key=to_lux)

def adjust_hex_color(hex_color, delta=5):
    # Ensure the hex color starts with a '#'
    if not hex_color.startswith('#'):
        raise ValueError("Invalid hex color format.")

    # Extract the R, G, B values
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    # Add the delta and clamp the values between 0 and 255
    r = max(0, min(255, r + delta))
    g = max(0, min(255, g + delta))
    b = max(0, min(255, b + delta))

    # Convert back to hex format and return
    return "#{:02x}{:02x}{:02x}".format(r, g, b)