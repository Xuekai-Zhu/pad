def solution():
    # Define the total number of people at camp
    total_people = 133

    # Define the difference between the number of boys and girls
    boy_girl_difference = 33

    # Calculate the number of boys
    num_boys = (total_people + boy_girl_difference) / 2

    # Calculate the number of girls
    num_girls = total_people - num_boys

    result = num_girls
    return result

print(solution())