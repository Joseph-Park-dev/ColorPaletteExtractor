# Color Palette Extractor

## Overview
This program extracts colors from an image and saves them as a .png color palette.

## How to install
If you have downloaded the .exe file, you can run it without installation.

## How to use
1. Insert the image path into the input box, or select an image file by clicking the "Browse..." button.
2. Set the background color. The empty space in the palette image will be filled with this RGB value.
3. Set Color Count, the number of colors displayed on the result palette.
3. Press "Extract Color Palette" and enter a file name for the .png palette.
4. The .png file will be displayed along with a color analysis. The saved file will be located in the directory you have set.

### Color Count?
The number of extracted colors displayed in the palette. Colors with the largest proportions are shown first from the left.

### Background?
Background color for the generated palette. Empty space will be filled with this color.

## Program's life
### 2025.09.16 (v.0.1.0 - Removed)
Core features were implemented. The project was uploaded to the GitHub repository.

### 2025.09.17 (v.0.1.1)
GUIs for setting values (tolerance & limit) were added.
GUI alignment was revised for a better appearance.
Bugs were fixed.

### 2026.06.08 (v.0.2.0)
"limit" was renamed to "Color Count" for better clarity.
"extcolors" was removed from the project. PIL is now used for simplicity.
Bugs were fixed and the program works better!

## Developer Contact
This program was made by GooCat Studio as a utility to assist with video game development. <br>

JungBae Park
jbpark1654@gmail.com