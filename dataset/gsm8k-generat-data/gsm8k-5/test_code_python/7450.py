def solution():
    total_campers = 96  # There are 96 campers at camp Wonka
    boys = int(total_campers * (2/3))  # Two-thirds of the campers are boys
    girls = total_campers - boys  # The remaining one-third are girls

    # Calculate the number of boys and girls who want to toast marshmallows
    boys_toast = int(boys * 0.5)
    girls_toast = int(girls * 0.75)

    # Calculate the total number of marshmallows needed
    total_toast = boys_toast + girls_toast
    result = total_toast
    return result

print(solution())