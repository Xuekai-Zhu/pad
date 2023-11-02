def solution():
    """A bag of dozen apples costs $14 and Brian has already spent $10 on kiwis and half that much on bananas. What's the maximum number of apples Brian can buy if he left his house with only $50 and needs to pay the $3.50 subway fare each way?"""
    apple_cost = 14
    kiwi_cost = 10
    banana_cost = kiwi_cost / 2
    subway_round_trip_cost = 3.5 * 2
    max_budget_for_apples = 50 - kiwi_cost - banana_cost - subway_round_trip_cost
    max_apples = max_budget_for_apples // apple_cost
    result = max_apples
    return result

print(solution())