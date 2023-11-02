def solution():
    # Define the variables
    refilled_amount = 10
    used_amount = 20
    end_amount = 60

    # Calculate the number of refills
    num_refills = (end_amount - refilled_amount) // (refilled_amount - used_amount)

    # Calculate the initial amount of wipes
    initial_amount = end_amount + num_refills * (refilled_amount - used_amount)

    # Return the initial amount
    result = initial_amount
    return result

print(solution())