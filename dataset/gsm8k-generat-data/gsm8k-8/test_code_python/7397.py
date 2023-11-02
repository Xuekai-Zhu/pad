def solution():
    # Define the total amount needed for the business
    total_amount = 1000

    # Define the amount already raised
    amount_raised = 200

    # Calculate the remaining amount needed
    remaining_amount = total_amount - amount_raised

    # Calculate the number of people needed to fund the remaining amount
    num_people = remaining_amount / 10

    # Round up to the nearest whole number
    num_people = math.ceil(num_people)

    result = num_people
    return result

print(solution())