import random


""""""


def generate_warmup(category):
    
    warmup_length = 0
    strokes = ["Free", "Back", "Breast", "IM"]
    distances = [100, 200, 300, 400]
    repetitions = [1, 2, 3, 4]


    if category == "easy":
        max_warmup_length = 200
    elif category == "normal":
        max_warmup_length = 400
    elif category == "hard":
        max_warmup_length = 600

    warmup_exercises = []


    # keep adding elements to the warmup list until the max_warmup_length is not reached 
    while warmup_length != max_warmup_length:
        stroke = random.choice(strokes)
        distance = random.choice(distances)

        # Calculate possible repetitions that fit within the remaining capacity
        remaining_capacity = max_warmup_length - warmup_length
        possible_repetitions = [r for r in repetitions if r * distance <= remaining_capacity]

        if possible_repetitions:
            # Choose a valid repetition count
            repetition = random.choice(possible_repetitions)
            total_distance = repetition * distance

            warmup_length += total_distance
            warmup_exercises.append(f"{repetition} x {distance}m {stroke}")

        # If no valid repetition exists, try another distance or break
        else:
            # Try to find a single exact match for remaining capacity
            if remaining_capacity in distances:
                warmup_exercises.append(f"1 x {remaining_capacity}m {random.choice(strokes)}")
                warmup_length += remaining_capacity
                continue
            else:
                continue  # Exit if no valid options remain

    return warmup_length, warmup_exercises


