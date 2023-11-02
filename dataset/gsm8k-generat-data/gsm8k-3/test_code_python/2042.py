def solution():
    """The PTA had saved $400 set aside after a fundraising event. They spent a fourth of the money on school supplies. Then they spent half of what was left on food for the faculty. How much money did they have left?"""
    # Define the initial amount saved
    initial_amount = 400

    # Calculate the amount spent on school supplies
    school_supplies = initial_amount / 4

    # Calculate the amount left after buying school supplies
    amount_left = initial_amount - school_supplies

    # Calculate the amount spent on food for the faculty
    food = amount_left / 2

    # Calculate the final amount left
    final_amount = amount_left - food

    # Display the final amount left
    result = final_amount
    return result

print(solution())