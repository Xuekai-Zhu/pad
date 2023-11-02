def solution():
    """Ali and Leila reserve their places for a trip to Egypt. The price is $147 per person, but they were each given a discount of $14 since there are two of them. How much does their trip cost?"""
    price_per_person = 147
    discount_per_person = 14
    num_people = 2
    cost_before_discount = price_per_person * num_people
    cost_after_discount = cost_before_discount - (discount_per_person * num_people)
    result = cost_after_discount
    return result

print(solution())