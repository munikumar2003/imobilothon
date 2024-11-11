from car_system import CarDoorAlarmSystem

def main():
    alarm_system = CarDoorAlarmSystem()
    print("Starting Car Door Alarm System...")
    while True:
        command = input("\nEnter 'lock' to lock car, 'unlock' to unlock car, or 'exit' to stop: ").strip().lower()
        if command == 'lock':
            alarm_system.lock_car()
        elif command == 'unlock':
            alarm_system.unlock_car()
        elif command == 'exit':
            print("Exiting Car Door Alarm System...")
            break
        else:
            print("Invalid command. Please enter 'lock', 'unlock', or 'exit'.")

if __name__ == "__main__":
    main()
