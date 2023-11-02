def solution():
    """A seminar is offered to a school for their teachers. The regular seminar fee is $150 but they offer a 5% discount if they register 2 days before the scheduled seminar. The school registered 10 teachers for the seminar a week before the schedule and it also released a $10 food allowance for each of the teachers. How much did the school spend in all?"""
    seminar_fee = 150
    discount = 0.05
    registration_fee = seminar_fee - (seminar_fee * discount)
    num_teachers = 10
    food_allowance = 10
    total_fee = (registration_fee + food_allowance) * num_teachers
    result = total_fee
    return result

print(solution())