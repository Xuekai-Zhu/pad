def solution():
    """A seminar is offered to a school for their teachers. The regular seminar fee is $150 but they offer a 5% discount if they register 2 days before the scheduled seminar. The school registered 10 teachers for the seminar a week before the schedule and it also released a $10 food allowance for each of the teachers. How much did the school spend in all?"""
    num_teachers = 10
    seminar_fee = 150
    discount_percent = 5
    discount_amount = seminar_fee * (discount_percent / 100)
    discounted_fee = seminar_fee - discount_amount
    food_allowance = 10
    total_cost = (discounted_fee * num_teachers) + (food_allowance * num_teachers)
    result = total_cost
    return result

print(solution())