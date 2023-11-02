def solution():
    """A bag of dozen apples costs $14 and Brian has already spent $10 on kiwis and half that much on bananas. What's the maximum number of apples Brian can buy if he left his house with only $50 and needs to pay the $3.50 subway fare each way?"""
    apple_cost = 14
    kiwi_cost = 10
    banana_cost = kiwi_cost / 2
    subway_fare_per_trip = 3.5
    money_left_after_transportation = 50 - (2 * subway_fare_per_trip)
    max_apples = int(money_left_after_transportation // apple_cost)
    result = max_apples
    return result

print(solution())