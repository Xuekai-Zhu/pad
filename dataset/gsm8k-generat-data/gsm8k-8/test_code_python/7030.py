def solution():
    # Set the initial number of cherry sours
    cherry_sours = 32

    # Calculate the number of lemon sours based on the 4:5 ratio
    lemon_sours = int((5/4) * cherry_sours) - cherry_sours

    # Calculate the number of orange sours based on the 25% proportion
    total_sours = cherry_sours + lemon_sours
    orange_sours = int(0.25 * total_sours)

    # Calculate the total number of sours
    total_sours += orange_sours

    result = total_sours
    return result

print(solution())