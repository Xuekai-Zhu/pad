def solution():
    jay_guests = 22
    gloria_guests = 36
    total_guests = jay_guests + gloria_guests

    # Calculate the number of flags they need
    total_flags = total_guests + 2  # Add 2 for Jay and Gloria

    # Calculate the number of sets of 5 flags needed
    sets_of_flags = total_flags // 5

    # Calculate the total cost of the flags
    flag_cost = sets_of_flags * 1.0

    result = flag_cost
    return result

print(solution())