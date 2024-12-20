import random

"""
This file generates the warm-up part of the training plan.
"""

def generate_warmup(category):
    """
    Generate a warm-up set with exercises based on the difficulty category.
    Returns the total warm-up length and a list of exercises.
    """
    warmup_length = 0  # Initialize the total warm-up length
    strokes = ["Free", "Back", "Breast", "IM"]  # Types of swimming strokes (IM = Individual Medley)
    distances = [100, 200, 300, 400]  # Possible distances for each repetition
    repetitions = [1, 2, 3, 4]  # Possible repetitions for each exercise

    # Set the maximum length of the warm-up based on the selected category
    if category == "easy":
        max_warmup_length = 200
    elif category == "normal":
        max_warmup_length = 400
    elif category == "hard":
        max_warmup_length = 600
  

    warmup_exercises = []  # List to store generated warm-up exercises

    # Generate exercises until the total length reaches the maximum allowed
    while warmup_length != max_warmup_length:
        stroke = random.choice(strokes)  # Randomly select a stroke
        distance = random.choice(distances)  # Randomly select a distance

        # Calculate the remaining capacity and filter repetitions that fit within it
        remaining_capacity = max_warmup_length - warmup_length
        possible_repetitions = [r for r in repetitions if r * distance <= remaining_capacity]

        if possible_repetitions:
            # Randomly choose a valid repetition count
            repetition = random.choice(possible_repetitions)
            total_distance = repetition * distance
            warmup_length += total_distance  # Update the total length
            warmup_exercises.append(f"{repetition} x {distance}m {stroke}")  # Add exercise description

        else:
            # Handle edge case where no valid repetition exists
            if remaining_capacity in distances:
                warmup_exercises.append(f"1 x {remaining_capacity}m {random.choice(strokes)}")
                warmup_length += remaining_capacity
            else:
                continue  # Retry with a new random selection if no valid options remain

    return warmup_length, warmup_exercises



