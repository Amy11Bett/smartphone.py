# OOP Assignment - Python

## Overview

This repository contains the code for the Object-Oriented Programming (OOP) assignment, where we designed and implemented classes and explored polymorphism and inheritance.

### Assignment 1: Design Your Own Class! 🏗️

In this part of the assignment, I created a **Smartphone** class with basic functionalities like making calls, checking battery life, and charging. Additionally, I implemented an inheritance structure with a **SmartphoneWithCamera** class, which inherits from the Smartphone class and adds camera-specific features like taking pictures.

#### Classes:
- **Smartphone**: Represents a basic smartphone with methods like `make_call()`, `check_battery()`, and `charge()`.
- **SmartphoneWithCamera**: Inherits from the Smartphone class and overrides the `make_call()` method to demonstrate polymorphism and adds the `take_picture()` method.

### Activity 2: Polymorphism Challenge! 🎭

For this activity, I created two vehicle classes (`Car` and `Plane`) that each implement their own version of the `move()` method. This demonstrates polymorphism in Python, where each class defines the same method but with different behavior.

#### Classes:
- **Vehicle**: A base class with a generic `move()` method.
- **Car**: Inherits from the `Vehicle` class and overrides the `move()` method to print a message about driving.
- **Plane**: Inherits from the `Vehicle` class and overrides the `move()` method to print a message about flying.

### How to Run the Program

1. Clone or download the repository to your local machine.
2. Open a terminal/command prompt and navigate to the directory where the files are located.
3. Run the Python files using the following commands:

   ```bash
   python smartphone_and_camera.py
   python polymorphism.py
