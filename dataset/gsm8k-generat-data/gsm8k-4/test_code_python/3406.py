def solution():
    """Isabelle works in a hotel and runs a bubble bath for each customer who enters the hotel. There are 13 rooms for couples and 14 single rooms. For each bath that is run, Isabelle needs 10ml of bubble bath. If every room is filled to maximum capacity, how much bubble bath, in millilitres, does Isabelle need?"""
    # Define the number of rooms for couples and single rooms
    COUPLE_ROOMS = 13
    SINGLE_ROOMS = 14

    # Define the amount of bubble bath required for each bath
    BUBBLE_BATH_PER_BATH = 10

    # Calculate the total number of baths needed
    total_baths = COUPLE_ROOMS * 2 + SINGLE_ROOMS

    # Calculate the total amount of bubble bath needed
    total_bubble_bath = total_baths * BUBBLE_BATH_PER_BATH

    # return the result
    result = total_bubble_bath
    return result

print(solution())