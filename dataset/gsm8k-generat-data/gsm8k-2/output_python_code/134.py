def solution():
    """A couple with two children, ages 6 and 10 years old, decided to go to an amusement park. The regular ticket costs $109, but children below 12 years old have a $5 discount. If they gave the cashier $500, how much change will they receive?"""
    regular_price = 109
    child_discount = 5
    adult_price = regular_price
    child1_price = regular_price - child_discount
    child2_price = regular_price - child_discount
    total_price = adult_price + child1_price + child2_price
    change = 500 - total_price
    result = change
    return result

print(solution())