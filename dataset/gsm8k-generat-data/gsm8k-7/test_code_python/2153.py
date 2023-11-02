def solution():
    flour = 2
    white_sugar = 1
    brown_sugar = 0.25
    oil = 0.5
    measuring_scoop = 0.25

    # Calculate the total number of times Felicia needs to fill the scoop
    total_scoops = (flour + white_sugar + brown_sugar + oil) / measuring_scoop

    result = total_scoops
    return result

print(solution())