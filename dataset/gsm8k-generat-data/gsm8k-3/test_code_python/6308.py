def solution():
    """Mr. Dubois buys a new car for $13,380. He pays $5,400 and pays the rest by giving $420 a month. In how many months will the car be fully paid for?"""
    # Define the initial cost of the car and the amount paid upfront
    INITIAL_COST = 13380
    UPFRONT_PAYMENT = 5400

    # Calculate the remaining amount to be paid
    remaining_amount = INITIAL_COST - UPFRONT_PAYMENT

    # Calculate the number of months it will take to fully pay for the car
    months_to_pay = remaining_amount / 420

    # Display the number of months
    result = months_to_pay
    return result

print(solution())