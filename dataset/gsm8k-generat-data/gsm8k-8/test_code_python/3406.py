def solution():
    # Calculate the total number of baths needed in the couples rooms
    couples_baths = 2 * 13

    # Calculate the total number of baths needed in the single rooms
    single_baths = 14

    # Calculate the total number of baths needed
    total_baths = couples_baths + single_baths

    # Calculate the total amount of bubble bath needed
    bubble_bath_needed = total_baths * 10
    result = bubble_bath_needed
    return result

print(solution())