# Blender Driver Constraint Addon
![Beyond Driver Constraint Addon](https://github.com/user-attachments/assets/e0d7f814-c1cc-40cf-ae08-d4e8eecc13b1)
## Description
This Blender addon allows users to easily set up complex drivers with just a few clicks. It supports relationships between object properties, shape keys, and bone transformations. It provides advanced functionality for creating drivers and action constraints in Blender.

## Features
- Easily create drivers for various property types (object, mesh, material, bone, etc.)
- Set up action constraints for bones
- Automatic limit detection for drivers
- Support for custom properties drivers anywhere in blender
- Interpolation type selection for drivers
- Easy flipping of driver and property limits
- Option to set driver limit constraints

## Installation
1. Download the addon file (`driver_constraint_creator.py`)
2. Open Blender and go to Edit > Preferences > Add-ons
3. Click "Install" and select the downloaded file
4. Enable the addon by checking the box next to its name

## Usage
1. Right click the property you want to drive and click "copy full data path"
2. Transform an object or bone to where your driver value should be 1.0
3. Right Click the object/bone and select "Driver Contstraint" in the menu
4. Fill in the required fields:
   - For Drivers: Property path, transform type, space, limits, etc.
   - For Actions: Action name, transform type, space, frame range, etc.
5. Click "Create Driver Constraint" to apply the settings

## Tips
- Use the clipboard to quickly input property paths
- The addon can automatically detect appropriate limits for drivers
- You can easily flip driver and property limits using the provided buttons
- For action constraints, you can add new ones or delete existing ones in batch

## Requirements
- Blender 2.80 or newer

## License
This addon is released under the GNU General Public License v3.0.

## Credits
Created by Andreas Esau and modified by Tyler Walker to support any property type.

## Support
For issues, feature requests, or contributions, please visit the addon's repository [insert repository link here].