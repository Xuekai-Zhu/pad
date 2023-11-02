def solution():
    """Emma got $2000 from the bank. She bought $400 of furniture and gave 3/4 of the rest to her friend Anna. How much is left with Emma?"""
    # Define the initial amount Emma got from the bank
    initial_amount = 2000

    # Define the cost of furniture
    furniture_cost = 400

    # Calculate the amount left after buying furniture
    amount_left = initial_amount - furniture_cost

    # Calculate the amount Emma gave to her friend
    amount_given = 0.75 * amount_left

    # Calculate the amount left with Emma
    amount_left_emma = amount_left - amount_given

    # Display the amount left with Emma
    result = amount_left_emma
    return result

print(solution())