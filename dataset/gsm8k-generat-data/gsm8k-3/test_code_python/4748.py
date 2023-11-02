def solution():
    """There was some money in the cookie jar. Doris spent $6 from the cookie jar. Martha spent half as much as Doris. If there were $15 left in the cookie jar, how much money, in dollars, was there in the cookie jar at first?"""
    # Define the amount Doris spent
    doris_spent = 6

    # Calculate the amount Martha spent
    martha_spent = doris_spent / 2

    # Calculate the total amount spent
    total_spent = doris_spent + martha_spent

    # Calculate the amount left in the cookie jar
    amount_left = 15

    # Calculate the amount in the cookie jar at first
    amount_at_first = total_spent + amount_left

    # Display the amount in the cookie jar at first
    result = amount_at_first
    return result

print(solution())