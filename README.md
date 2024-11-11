# Car Door Alarm System

## Project Overview

The **Car Door Alarm System** is designed to prevent accidental harm to living organisms (like pets, children, or other passengers) that may be left inside a locked car. The system uses simulated motion and heat sensors to detect if any living being is still in the car once it’s locked. If an occupant is detected, the system triggers visual, audible, and mobile alerts to notify the driver or passersby to prevent potential hazards such as overheating or suffocation.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Files](#files)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Structure
```plaintext
car_door_alarm_system/
├── main.py
├── car_system.py
├── sensors.py
├── alerts.py
├── logger.py
└── README.md
```
## Features
**Vital Detection Sensors:** Detects motion and heat within the car when locked.
**Alert System:**
**Visual and Audible Alerts**: Flashing lights and alarm sounds notify nearby individuals.
**Mobile Notification:** A simulated mobile notification informs the driver of potential hazards inside the car.
**Smart Integration with Car Systems:** Simulates smart interaction with the car’s lock and key fob systems.
**Logging**: All major actions are logged to track system events.

## Requirements
Python 3.x
Logging Library: Included in Python’s standard library.

## Installation and Setup
Clone the repository:

**bash**
git clone https://github.com/munikumar2003/imobilothon/


Install dependencies:
This project uses Python’s standard libraries, so no additional dependencies are required.

## Usage
Run the system using:

bash
Copy code
python main.py
Interact with the program by locking and unlocking the car using commands:

lock: Lock the car and activate occupant detection.
unlock: Unlock the car and deactivate alerts.
exit: Exit the program.
The system will check for occupants based on simulated motion and heat sensors. If both are detected, it will trigger:

Visual alert (Flashing lights)
Audible alert (Alarm sound)
Mobile notification to simulate driver alert

## Files
main.py: Main script to run the system and handle user commands.
car_system.py: Contains the CarDoorAlarmSystem class, which manages the core functionality and alert triggers.
sensors.py: Simulates the motion and heat sensors.
alerts.py: Handles all alerts (visual, audible, and mobile).
logger.py: Configures logging, storing all events in car_alarm_system.log for easy review.
