def solution():
    """Felicia is baking a cake. She needs 2 cups of flour, a cup of white sugar, a 1/4 cup of brown sugar, and a 1/2 cup of oil. Her only measuring scoop is 1/4 cup. How many times does she fill it to complete the measurements?"""
    # Define the amounts of each ingredient needed
    flour = 2
    white_sugar = 1
    brown_sugar = 0.25
    oil = 0.5

    # Define the size of the measuring scoop
    scoop = 0.25

    # Count the number of times the scoop is used for each ingredient
    flour_scoops = flour / scoop
    white_sugar_scoops = white_sugar / scoop
    brown_sugar_scoops = brown_sugar / scoop
    oil_scoops = oil / scoop

    # Get the total number of times the scoop was used
    total_scoops = flour_scoops + white_sugar_scoops + brown_sugar_scoops + oil_scoops

    # Display the total number of times the scoop was used
    result = total_scoops
    return result

print(solution())