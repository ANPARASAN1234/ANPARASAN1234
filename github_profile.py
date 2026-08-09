from PIL import Image, ImageDraw, ImageFont

# ==============================
# SETTINGS
# ==============================

SIZE = 500
BACKGROUND = (10, 15, 25)
WHITE = (255, 255, 255)
CYAN = (0, 220, 255)

FRAMES = 60
FRAME_DURATION = 60

# ==============================
# FONT
# ==============================

# Windows font
FONT_PATH = "C:/Windows/Fonts/arial.ttf"
BOLD_FONT_PATH = "C:/Windows/Fonts/arialbd.ttf"

try:
    title_font = ImageFont.truetype(BOLD_FONT_PATH, 48)
    code_font = ImageFont.truetype(BOLD_FONT_PATH, 80)
except:
    title_font = ImageFont.load_default()
    code_font = ImageFont.load_default()


# ==============================
# CREATE FRAMES
# ==============================

frames = []

for frame_number in range(FRAMES):

    # Create image
    img = Image.new(
        "RGB",
        (SIZE, SIZE),
        BACKGROUND
    )

    draw = ImageDraw.Draw(img)

    # --------------------------------
    # CENTER
    # --------------------------------

    center_x = SIZE // 2
    center_y = SIZE // 2

    # --------------------------------
    # CIRCULAR BORDER
    # --------------------------------

    # Drawing progress
    progress = int((frame_number + 1) / FRAMES * 360)

    draw.arc(
        [35, 35, 465, 465],
        start=-90,
        end=-90 + progress,
        fill=CYAN,
        width=8
    )

    # --------------------------------
    # SECOND CIRCLE
    # --------------------------------

    draw.arc(
        [50, 50, 450, 450],
        start=0,
        end=360,
        fill=(80, 90, 110),
        width=2
    )

    # --------------------------------
    # CODE SYMBOL </> 
    # --------------------------------

    code_text = "</>"

    bbox = draw.textbbox(
        (0, 0),
        code_text,
        font=code_font
    )

    code_width = bbox[2] - bbox[0]
    code_height = bbox[3] - bbox[1]

    code_x = center_x - code_width // 2
    code_y = center_y - code_height - 20

    draw.text(
        (code_x, code_y),
        code_text,
        font=code_font,
        fill=WHITE
    )

    # --------------------------------
    # ANPARASAN TEXT
    # --------------------------------

    name = "ANPARASAN"

    # Number of visible characters
    visible_chars = int(
        len(name) * (frame_number + 1) / FRAMES
    )

    visible_name = name[:visible_chars]

    bbox = draw.textbbox(
        (0, 0),
        visible_name,
        font=title_font
    )

    text_width = bbox[2] - bbox[0]

    text_x = center_x - text_width // 2
    text_y = center_y + 35

    draw.text(
        (text_x, text_y),
        visible_name,
        font=title_font,
        fill=CYAN
    )

    # --------------------------------
    # DEVELOPER TEXT
    # --------------------------------

    developer = "FULL-STACK DEVELOPER"

    small_font = ImageFont.truetype(
        FONT_PATH,
        18
    )

    bbox = draw.textbbox(
        (0, 0),
        developer,
        font=small_font
    )

    small_width = bbox[2] - bbox[0]

    draw.text(
        (
            center_x - small_width // 2,
            420
        ),
        developer,
        font=small_font,
        fill=(180, 190, 200)
    )

    # Add frame
    frames.append(img)


# ==============================
# SAVE GIF
# ==============================

frames[0].save(
    "ANPARASAN_GitHub_Profile.gif",
    save_all=True,
    append_images=frames[1:],
    duration=FRAME_DURATION,
    loop=0,
    optimize=True
)

print("================================")
print("GitHub profile animation created!")
print("File: ANPARASAN_GitHub_Profile.gif")
print("================================")