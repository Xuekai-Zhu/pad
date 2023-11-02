def solution():
    """The total cost of staying at High Services Hotel is $40 per night per person. Jenny and two of her friends went to the hotel and stayed for three nights. What's the total amount of money they all paid together?"""
    cost_per_night_per_person = 40
    number_of_people = 3
    number_of_nights = 3
    total_cost = cost_per_night_per_person * number_of_people * number_of_nights
    result = total_cost
    return result

print(solution())