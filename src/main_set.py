import random

def generate_main_set(category, materials):
    """
    Generate a swim main set with exercises based on difficulty category and materials provided.
    Returns the total main set length and a list of exercises.
    """
    mainset_length = 0
    strokes = ["Free", "Back", "Breast", "Fly", "IM"]  # Types of swimming strokes (IM = Individual Medley)
    material_list = materials  # List of materials available for swimming exercises
    distances = [25, 50, 100, 150, 200, 300, 400]  # Possible distances for each repetition
    exercise_types = [
        "single stroke",
        "two strokes",
        "kick",
        "drill",
        "kick with material",
        "drill with material",
        "swim with material",
    ]  # Types of exercises
    repetitions = [1, 2, 3, 4]  # Possible repetitions for each exercise

    # Determine the maximum length of the main set based on the selected difficulty category
    if category == "easy":
        max_mainset_length = 1200
    elif category == "normal":
        max_mainset_length = 2000
    elif category == "hard":
        max_mainset_length = 3000
     # Ensures valid input

    main_set_exercises = []  # List to store generated exercises

    # Generate exercises until the total length reaches the maximum allowed
    while mainset_length != max_mainset_length:
        stroke = random.choice(strokes)  # Randomly select a stroke
        distance = random.choice(distances)  # Randomly select a distance
        exercise_type = random.choice(exercise_types)  # Randomly select an exercise type

        # Calculate the remaining capacity and filter repetitions that fit within it
        remaining_capacity = max_mainset_length - mainset_length
        possible_repetitions = [r for r in repetitions if r * distance <= remaining_capacity]

        if possible_repetitions:
            # Randomly choose a valid repetition count
            repetition = random.choice(possible_repetitions)
            total_distance = repetition * distance
            mainset_length += total_distance  # Update the total length

            # Generate the exercise description based on the type
            match exercise_type:
                case "single stroke":
                    main_set_exercises.append(f"{repetition} x {distance}m {stroke} at ")

                case "two strokes":
                    second_stroke = random.choice(strokes)
                    main_set_exercises.append(
                        f"{repetition} x {distance}m ({distance // 2} {stroke}/{distance // 2} {second_stroke})"
                    )

                case "kick":
                    main_set_exercises.append(f"{repetition} x {distance}m {stroke}, kick")

                case "drill":
                    main_set_exercises.append(f"{repetition} x {distance}m {stroke}, drills")

                case "swim with material":
                    material = random.choice(material_list)
                    main_set_exercises.append(f"{repetition} x {distance}m {stroke}, w/ {material}")

                case "kick with material":
                    material = random.choice(material_list)
                    main_set_exercises.append(f"{repetition} x {distance}m {stroke}, kick, w/ {material}")

                case "drill with material":
                    material = random.choice(material_list)
                    main_set_exercises.append(f"{repetition} x {distance}m {stroke}, drills, w/ {material}")

        else:
            # Handle edge case where no valid repetition exists
            if remaining_capacity in distances:
                main_set_exercises.append(f"1 x {remaining_capacity}m {random.choice(strokes)}")
                mainset_length += remaining_capacity
            else:
                continue  # Retry with a new random selection if no valid options remain

    return mainset_length, main_set_exercises






