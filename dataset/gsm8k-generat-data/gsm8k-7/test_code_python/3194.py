def solution():
    total_guests = 1000
    married_percent = 0.3
    single_percent = 0.5

    # Calculate the number of married guests
    num_married = total_guests * married_percent

    # Calculate the number of single guests
    num_single = total_guests * single_percent

    # Calculate the number of children guests
    num_children = total_guests - num_married - num_single

    # Calculate the difference between the number of married and children guests
    difference = num_married - num_children
    result = difference
    return result

print(solution())