# Text-Fabrication
This repository is about the Data Fabrication Technique to generate a variations in character numbers and symbols are necessary. For this, a blank image is used as the canvas, and the text fonts are loaded. Random characters are generated from these loaded fonts in the batch code format. By randomly arranging the batch code positions from horizontal and vertical and applying random rotation angles, this technique generates a high degree of randomization. As a result, a variety of data are used to make the both text detection and recognition model more generalized and robust.

Process of data fabrication:
1) Check and Create Output Directory
2) Define a function to generate random characters i.e. generates a random string of characters (letters, numbers, and symbols) of a specified length.
3) Define a function to get the text dimensions(height,width) of a text.
4) Define a function to create the data
    a) Load the text font
    b) Generates the random text in the required format for each line
    c) Sets the coordinates to place the text
    d) Generates the angle of rotation from rot_ang.
    e) Call the draw_rotated_text function which return rotated image.

    Image Rotation
    1) To rotate the image "draw_rotated_text" function is used. First we take the height and width of the input image, then calculates the maximum dimension of the image( either height or width) this is done to create a enough space to rotate the text without being cut off at the edges in transparency mask.

    2) Create a transparency mask in which all its pixels are set to transparent, which means their values are set to 0

    3) Creates a drawing object on the transparency mask using the ImageDraw.Draw() method. This object provides various methods for drawing shapes, lines, and text onto an image.

    4) Draws the text on the transparency mask at a specific position with white color (255). The text will appear as white against the transparent background because white color text will be clearly visible and easily separable from the background when blended onto the final image.

    5) If the angle is a multiple of 90 degrees, it directly rotates the transparency mask by that angle. This is a straightforward operation and can be done without much distortion. Otherwise, it enlarges the mask, rotates it, and then resizes it back to the original size to minimize distortion. 
        a) First, it enlarges the transparency mask by a factor of 8 in both dimensions. This enlargement provides more detail for the rotation operation and helps minimize distortion.
        b) Rotates the enlarged mask by the desired angle. This rotation operation is performed on the enlarged mask, which helps preserve the text's quality.
        c) After rotating, the code resizes the mask back to its original size using a high-quality resampling method (Image.LANCZOS). This resizing operation restores the mask to its original dimensions while retaining the benefits of the rotation and enlargement steps.

    6) Calculates the bounding box for the rotated mask to match the size of the input image.

    7) Now crops the rotated mask to match the size of the input image.

    8) Creates a new image filled with the specified color and transparency.

    9) Pastes this color-filled image onto the original input image using the cropped rotated mask as a transparency mask.

    10) Finally, it returns the modified image with the text drawn at the specified angle.

5) Set the image name and text name save the image.
6) Here the angle of rotation is negative because the rotation direction is opposite for coordinate systems used in PIL and trigonometric functions.
7) Set four corner points for unrotated bounding box:-
    top_left1: Top-left corner of the rectangle.
    top_right1: Top-right corner of the rectangle.
    bottom_left1: Bottom-left corner of the rectangle.
    bottom_right1: Bottom-right corner of the rectangle.
8) Rotation angle is converted from degrees to radians because trigonometric functions in Python's math module work with radians.
9) sin_angle1 = math.sin(angle_rad1) and cos_angle1 = math.cos(angle_rad1): The sine and cosine of the rotation angle are calculated.
These values are needed to rotate the corner points of the rectangle around the center point.
10) The corner points are rotated around the center point of the rectangle using the rotation formula:
x'=x⋅cos(θ)−y⋅sin(θ)
y'=x⋅sin(θ)+y⋅cos(θ)
For each corner point:
If the angle is negative, it means the rotation is clockwise.
If the angle is positive, it means the rotation is counterclockwise.
rotated_top_left1, rotated_top_right1, rotated_bottom_left1, and rotated_bottom_right1 are the rotated corner points of the rectangle.
11) Create a annotation files from the rotated coordinates points in the format of (x1,y1,x2,y2,x3,y3,x4,y4) and save the annotation files in text files
12) Repeat the same process for other lines.

####
<img alt = 'coding' width = "1000" height = "500" src = "https://github.com/lalchhabi/Text-Fabrication/blob/master/fabrication_image.png">
