def solution():
    """Apples used to cost $1.6 per pound. The price got raised 25%. How much does it cost to buy 2 pounds of apples for each person in a 4 member family?"""
    original_price = 1.6
    price_increase = 0.25
    new_price = original_price * (1 + price_increase)
    pounds_per_person = 2
    number_of_people = 4
    total_pounds = pounds_per_person * number_of_people
    total_cost = new_price * total_pounds
    result = total_cost
    return result

print(solution())