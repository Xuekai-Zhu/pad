def solution():
    total_guests = 80
    num_men = 40
    num_women = num_men / 2
    num_children = total_guests - num_men - num_women

    # Add 10 children to the guest list
    num_children += 10

    result = num_children
    return result

print(solution())