from PIL import Image, ImageDraw, ImageFont

# Load input image and resize
input_image = Image.open('input.jpg')
resized_input_image = input_image.resize((360, 760))

# Define the size of the table
table_width = 340
table_height = 50

# Create a new image with a white background
image = Image.new('RGBA', (table_width, table_height), (255, 255, 255, 128))

# Define the font
font = ImageFont.truetype('times.ttf', 20)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the data for the table
table_data = [['WS', 'BS', 'S', 'T', 'Ini', 'A', 'D', 'I', 'WP', 'Fel'],
              ['51', '42', '32', '41', '24', '23', '45', '24', '15', '24']]

# Define the size of each cell
cell_width = table_width // len(table_data[0])
cell_height = table_height // len(table_data)

# Loop through the table data and draw the cells
for i in range(len(table_data)):
    for j in range(len(table_data[i])):
        # Calculate the coordinates of the cell
        x1 = j * cell_width
        y1 = i * cell_height
        x2 = (j + 1) * cell_width
        y2 = (i + 1) * cell_height
        
        # Draw the cell
        draw.rectangle((x1, y1, x2-1, y2-1), outline=(1, 1, 1))
        
        # Draw the text in the cell
        text_width, text_height = font.getsize(table_data[i][j])
        text_x = x1 + (cell_width - text_width) // 2
        text_y = y1 + (cell_height - text_height) // 2
        draw.text((text_x, text_y), table_data[i][j], fill=(0, 0, 0), font=font)

# Paste the output image onto the input image
table_x = (resized_input_image.width - table_width) // 2
table_y = (resized_input_image.height - table_height) // 2
resized_input_image.paste(image, (table_x, table_y), image)

# Save the image
resized_input_image.save('output.png')
