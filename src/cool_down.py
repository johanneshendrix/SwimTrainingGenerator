

# This function generates a cooldown length based on the difficulty category.
# The cooldown allows swimmers to perform their preferred activity to cool down.

def generate_cool_down(category):

    """
    Generate a cooldown length for the specified difficulty category.
    Returns a fixed distance depending on the category:
    - 'easy': 200 meters
    - 'normal': 400 meters
    - 'hard': 600 meters
    """

    if category == "easy":
        return 200
    elif category == "normal":
        return 400
    elif category == "hard":
        return 600

    




