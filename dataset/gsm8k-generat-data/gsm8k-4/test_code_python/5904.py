def solution():
    """Bill and Phil are firehouse Dalmatians. Bill has one less than twice as many spots as Phil. If they have 59 spots combined, how many spots does Bill have?"""
    # Define the number of spots on Phil
    phil_spots = None

    # Calculate the number of spots on Bill using the relationship defined in the problem
    bill_spots = 2 * phil_spots - 1

    # Calculate the total number of spots
    total_spots = bill_spots + phil_spots

    # Iterate over possible values of Phil's spots until the total number of spots is correct
    for i in range(1, total_spots):
        phil_spots = i
        bill_spots = 2 * phil_spots - 1
        if bill_spots + phil_spots == 59:
            break

    # Return the number of spots on Bill
    result = bill_spots
    return result

print(solution())