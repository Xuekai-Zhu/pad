def solution():
    num_adults = 58
    num_children = num_adults - 35
    num_seniors = num_children * 2

    # Calculate the total number of guests served
    total_guests = num_adults + num_children + num_seniors
    result = total_guests
    return result

print(solution())