def solution():
    # Define the required measurements
    flour = 2
    white_sugar = 1
    brown_sugar = 0.25
    oil = 0.5

    # Calculate the number of times the scoop is filled for each ingredient
    flour_scoops = flour / 0.25
    white_sugar_scoops = white_sugar / 0.25
    brown_sugar_scoops = brown_sugar / 0.25
    oil_scoops = oil / 0.25

    # Calculate the total number of times the scoop is filled
    total_scoops = flour_scoops + white_sugar_scoops + brown_sugar_scoops + oil_scoops
    result = total_scoops
    return result

print(solution())