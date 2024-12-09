import random



def generate_main_set(category, materials):
    
    mainset_length = 0
    strokes = ["Free", "Back", "Breast", "Fly", "IM"] #names of different strokes (IM = all strokes )
    material_list = materials  
    distances = [25, 50, 100, 150, 200, 300, 400] 
    exercise_types = ["single stroke", "two strokes", "kick", "drill", "kick with material", "drill with material", "swim with material"]
    repetitions = [1, 2, 3, 4]


    # depending on which category the user chooses, the max_length of the main set will defer
    if category == "easy":
        max_mainset_length = 1200
    elif category == "normal":
        max_mainset_length = 2000
    elif category == "hard":
        max_mainset_length = 3000

    main_set_exercises = []

    # keep adding elements to the main_set list until the max_mainset_length is not reached 
    while mainset_length != max_mainset_length:
        stroke = random.choice(strokes)
        distance = random.choice(distances)
        exercise_type = random.choice(exercise_types)

        # Calculate possible repetitions that fit within the remaining capacity
        remaining_capacity = max_mainset_length - mainset_length
        possible_repetitions = [r for r in repetitions if r * distance <= remaining_capacity]

        if possible_repetitions:
            # Choose a valid repetition count from the calculated values in possible_repetitions
            repetition = random.choice(possible_repetitions)
            total_distance = repetition * distance

            mainset_length += total_distance
            if exercise_type == "single stroke":
                main_set_exercises.append(f"{repetition} x {distance}m {stroke} at ")
            
            elif exercise_type == "two strokes":
                second_stroke = random.choice(strokes)
                main_set_exercises.append(f"{repetition} x {distance}m ({distance // 2} {stroke}/{distance // 2} {second_stroke})")
            elif exercise_type == "kick":
                main_set_exercises.append(f"{repetition} x {distance}m {stroke}, kick")

            elif exercise_type == "drill":
                main_set_exercises.append(f"{repetition} x {distance}m {stroke}, drills")

            elif exercise_type == "swim with material":
                material = random.choice(material_list)
                main_set_exercises.append(f"{repetition} x {distance}m {stroke}, w/ {material}")
            elif exercise_type == "kick with material":
                material = random.choice(material_list)
                main_set_exercises.append(f"{repetition} x {distance}m {stroke}, kick, w/ {material}")
            elif exercise_type == "drill with material":
                material = random.choice(material_list)
                main_set_exercises.append(f"{repetition} x {distance}m {stroke}, drills, w/ {material}")
            

        # If no valid repetition exists, try another distance or break
        else:
            # Try to find a single exact match for remaining capacity
            if remaining_capacity in distances:
                main_set_exercises.append(f"1 x {remaining_capacity}m {random.choice(strokes)}")
                mainset_length += remaining_capacity
                continue
            else:
                continue  # Exit if no valid options remain



    return mainset_length, main_set_exercises






