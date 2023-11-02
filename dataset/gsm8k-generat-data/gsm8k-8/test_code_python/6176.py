def solution():
    # Define the total number of kids
    total_kids = 34

    # Calculate the number of boys
    num_boys = (total_kids - 22) / 2

    # Calculate the number of girls
    num_girls = total_kids - num_boys

    result = num_girls
    return result

print(solution())