from __GUI__ import TkinterApp
import warm_up
import main_set
import cool_down

def main():
    # Launch the GUI and get user inputs
    app = TkinterApp()
    app.run()

    # Retrieve the selected values after the GUI closes
    available_equipment, training_type = app.get_values()

    # Generate the training plan
    warm_up_length, warm_up_exercises = warm_up.generate_warmup(training_type)
    mainset_length, mainset_exercises = main_set.generate_main_set(training_type, available_equipment)
    cool_down_length = cool_down.generate_cool_down(training_type)

    # Display the training plan
    print("\nHere is your training plan:")
    print("\nWarm-up:")
    for exercise in warm_up_exercises:
        print(exercise)

    print("\nMain set:")
    for exercise in mainset_exercises:
        print(exercise)

    print("\nCool down:")
    print(f"{cool_down_length}m choice")
    print(f"\nTotal Training Distance: {mainset_length + warm_up_length + cool_down_length}m")

if __name__ == "__main__":
    main()
