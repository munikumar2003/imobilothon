from sensors import detect_movement, detect_heat
from alerts import visual_alert, audible_alert, send_mobile_notification
from logger import setup_logging
import logging

# Initialize logging
setup_logging()

class CarDoorAlarmSystem:
    def __init__(self):
        self.movement_detected = False
        self.heat_detected = False
        self.is_car_locked = False
        self.occupant_detected = False
        self.temperature_threshold = 35.0  # Temperature threshold in Celsius

    def lock_car(self):
        self.is_car_locked = True
        print("Car is now locked.")
        logging.info("Car locked by the driver.")
        self.check_for_occupants()

    def unlock_car(self):
        self.is_car_locked = False
        self.occupant_detected = False
        print("Car is unlocked.")
        logging.info("Car unlocked by the driver.")

    def check_for_occupants(self):
        if self.is_car_locked:
            print("Checking for occupants...")
            self.movement_detected = detect_movement()
            self.heat_detected = detect_heat(self.temperature_threshold)
            if self.movement_detected and self.heat_detected:
                self.occupant_detected = True
                print("Warning: Potential occupant detected inside the car!")
                logging.warning("Occupant detected inside the locked car.")
                self.trigger_alert()
            else:
                print("No occupant detected. Car is secure.")
                logging.info("No occupant detected after locking.")

    def trigger_alert(self):
        if self.occupant_detected:
            visual_alert()
            audible_alert()
            send_mobile_notification()
