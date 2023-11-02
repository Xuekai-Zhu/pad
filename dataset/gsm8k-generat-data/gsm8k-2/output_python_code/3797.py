def solution():
    """John joins a country club with 3 other members of his family. The fee to join is $4000 per person. There is also a monthly cost of $1000 per person. John pays half the cost. How much does John pay for the first year?"""
    num_family_members = 4
    join_fee = 4000
    monthly_cost = 1000
    total_cost = (num_family_members * join_fee) + (12 * num_family_members * monthly_cost)
    john_cost = total_cost / 2
    result = john_cost
    return result

print(solution())