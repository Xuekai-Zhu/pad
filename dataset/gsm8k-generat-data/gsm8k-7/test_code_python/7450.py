def solution():
    num_campers = 96
    boys_ratio = 2/3
    girls_ratio = 1/3
    boys_toasting_ratio = 0.5
    girls_toasting_ratio = 0.75

    # Calculate the number of boys and girls at camp
    num_boys = num_campers * boys_ratio
    num_girls = num_campers * girls_ratio

    # Calculate the number of boys and girls who want to toast marshmallows
    num_boys_toasting = num_boys * boys_toasting_ratio
    num_girls_toasting = num_girls * girls_toasting_ratio

    # Calculate the total number of marshmallows needed
    total_marshmallows = num_boys_toasting + num_girls_toasting
    result = total_marshmallows
    return result

print(solution())