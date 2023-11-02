def solution():
    """Randy had $3,000. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. What was the value, in dollars, of the rest?"""
    # Define the initial amount Randy had
    initial_amount = 3000

    # Define the amount Smith gave Randy
    smith_amount = 200

    # Calculate the total amount Randy had after Smith gave him money
    total_amount = initial_amount + smith_amount

    # Define the amount Randy gave Sally
    sally_amount = 1200

    # Calculate the amount Randy kept
    kept_amount = total_amount - sally_amount

    # Return the result
    result = kept_amount
    return result

print(solution())