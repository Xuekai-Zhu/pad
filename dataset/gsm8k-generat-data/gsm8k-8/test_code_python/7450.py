def solution():
    # Calculate the number of boys and girls at the camp
    total_campers = 96
    boys = total_campers * (2/3)
    girls = total_campers * (1/3)

    # Calculate the number of boys and girls who want to toast marshmallows
    boys_toasting = boys * (50/100)
    girls_toasting = girls * (75/100)

    # Calculate the total number of marshmallows needed
    total_marshmallows = boys_toasting + girls_toasting
    result = total_marshmallows
    return result

print(solution())