def solution():
    """The total cost of staying at High Services Hotel is $40 per night per person. Jenny and two of her friends went to the hotel and stayed for three nights. What's the total amount of money they all paid together?"""
    rate_per_person_per_night = 40
    num_people = 3
    num_nights = 3
    total_cost = rate_per_person_per_night * num_people * num_nights
    result = total_cost
    return result

print(solution())