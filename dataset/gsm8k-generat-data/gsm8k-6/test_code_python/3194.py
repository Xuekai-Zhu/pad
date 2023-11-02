def solution():
    # Calculate the number of guests in each category
    married_guests = 0.3 * 1000
    single_guests = 0.5 * 1000
    children_guests = 1000 - married_guests - single_guests

    # Calculate the difference in the number of married guests and children guests
    difference = married_guests - children_guests
    result = difference
    return result

print(solution())