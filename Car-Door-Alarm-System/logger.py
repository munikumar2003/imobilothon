import logging

def setup_logging():
    logging.basicConfig(filename='car_alarm_system.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')
