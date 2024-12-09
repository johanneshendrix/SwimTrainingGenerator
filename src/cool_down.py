

#this function generates a cooldown length for each category, during the cool down a swimmer can simply do what they like to 
# cool down, which is why there are no further specifications on which strokes, material, etc.

def generate_cool_down(category):

    if category == "easy":
        return 200
    elif category == "normal":
        return 400
    elif category == "hard":
        return 600

    




