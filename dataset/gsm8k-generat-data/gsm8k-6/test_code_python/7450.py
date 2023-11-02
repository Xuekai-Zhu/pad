def solution():
    # Calculate the number of boys and girls at camp
    num_boys = (2/3) * 96
    num_girls = (1/3) * 96

    # Calculate the number of boys and girls that want to toast marshmallows
    boys_toast = 0.5 * num_boys
    girls_toast = 0.75 * num_girls

    # Calculate the total number of marshmallows needed
    total_toast = boys_toast + girls_toast

    result = total_toast
    return result

print(solution())