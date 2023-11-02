def solution():
    """Lucy plans to purchase potato chips for a party. Ten people will be at the party, including Lucy. The potato chips cost 25 cents per pound. How much will Lucy pay (in dollars) for the potato chips if she wants each person to get 1.2 pounds?"""
    num_people = 10
    chips_per_person = 1.2
    price_per_pound = 0.25
    total_pounds = num_people * chips_per_person
    total_price = total_pounds * price_per_pound
    result = total_price
    return result

print(solution())