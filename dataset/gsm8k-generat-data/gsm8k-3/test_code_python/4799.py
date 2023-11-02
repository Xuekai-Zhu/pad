def solution():
    """A seminar is offered to a school for their teachers. The regular seminar fee is $150 but they offer a 5% discount if they register 2 days before the scheduled seminar. The school registered 10 teachers for the seminar a week before the schedule and it also released a $10 food allowance for each of the teachers. How much did the school spend in all?"""
    # Define the regular seminar fee and discount rate
    REGULAR_FEE = 150
    DISCOUNT_RATE = 0.05

    # Calculate the discounted seminar fee if registered 2 days before
    discounted_fee = REGULAR_FEE - (REGULAR_FEE * DISCOUNT_RATE)

    # Calculate the cost of the seminar for 10 teachers
    seminar_cost = discounted_fee * 10

    # Calculate the cost of the food allowance for 10 teachers
    food_cost = 10 * 10

    # Calculate the total cost
    total_cost = seminar_cost + food_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())