def solution():
    """Annie goes to school. Today is her birthday, so Annie decided to buy some sweets for her colleagues. Every classmate got 2 candies. In the end, Annie got left with 12 candies. If there are 35 people in Annie's class in total, how much did Annie spend on candies, if one candy costs $0.1?"""
    classmates = 35
    candies_per_classmate = 2
    total_candies = classmates * candies_per_classmate + 12
    candy_price = 0.1
    total_cost = total_candies * candy_price
    result = total_cost
    return result

print(solution())