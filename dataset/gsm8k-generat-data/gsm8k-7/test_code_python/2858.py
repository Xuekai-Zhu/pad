def solution():
    total_guests = 60
    men = 15
    women = total_guests / 2
    children = total_guests - men - women

    # Calculate the number of men and children who left during the party
    men_left = men / 3
    children_left = 5

    # Calculate the number of guests who stayed for the whole party
    guests_stayed = total_guests - men_left - children_left

    result = guests_stayed
    return result

print(solution())