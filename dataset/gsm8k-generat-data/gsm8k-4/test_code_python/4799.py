def solution():
    """A seminar is offered to a school for their teachers. The regular seminar fee is $150 but they offer a 5% discount if they register 2 days before the scheduled seminar. The school registered 10 teachers for the seminar a week before the schedule and it also released a $10 food allowance for each of the teachers. How much did the school spend in all?"""
    # Define the regular seminar fee and the number of teachers registered
    fee_per_teacher = 150
    num_teachers = 10

    # Calculate the total seminar fee before the discount
    total_fee = fee_per_teacher * num_teachers

    # Apply the discount if applicable
    discount = 0
    if num_teachers >= 2 and num_teachers <= 9:
        discount = 0.05 * total_fee
        total_fee -= discount

    # Calculate the total cost, including the food allowance
    total_cost = total_fee + (num_teachers * 10)

    # return the result
    result = total_cost
    return result

print(solution())