def solution():
    """Apples used to cost $1.6 per pound. The price got raised 25%. How much does it cost to buy 2 pounds of apples for each person in a 4 member family?"""
    initial_price = 1.6
    percent_increase = 25
    new_price = initial_price * (1 + percent_increase / 100)
    pounds_per_person = 2
    members_in_family = 4
    total_cost = new_price * pounds_per_person * members_in_family
    result = total_cost
    return result

print(solution())