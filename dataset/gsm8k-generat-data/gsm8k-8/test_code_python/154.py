def solution():
    # Define the initial amounts in their accounts
    daniella_amount = 400
    ariella_amount = daniella_amount + 200

    # Calculate the interest earned by Ariella after two years
    ariella_interest = ariella_amount * 0.1 * 2

    # Add the interest earned to Ariella's initial amount
    total_ariella_amount = ariella_amount + ariella_interest

    # Return the final amount in Ariella's account after two years
    result = total_ariella_amount
    return result

print(solution())