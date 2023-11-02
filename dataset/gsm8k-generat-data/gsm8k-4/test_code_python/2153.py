def solution():
    """Felicia is baking a cake. She needs 2 cups of flour, a cup of white sugar, a 1/4 cup of brown sugar, and a 1/2 cup of oil. Her only measuring scoop is 1/4 cup. How many times does she fill it to complete the measurements?"""
    # Define the amounts needed for each ingredient
    flour = 2
    white_sugar = 1
    brown_sugar = 1/4
    oil = 1/2

    # Define the size of the measuring scoop
    scoop_size = 1/4

    # Calculate the number of times each scoop needs to be filled
    flour_scoops = int(flour / scoop_size)
    white_sugar_scoops = int(white_sugar / scoop_size)
    brown_sugar_scoops = int(brown_sugar / scoop_size)
    oil_scoops = int(oil / scoop_size)

    # Calculate the total number of times the scoop needs to be filled
    total_scoops = flour_scoops + white_sugar_scoops + brown_sugar_scoops + oil_scoops

    # return the result
    result = total_scoops
    return result

print(solution())