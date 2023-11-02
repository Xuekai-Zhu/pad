def solution():
    """Annie goes to school. Today is her birthday, so Annie decided to buy some sweets for her colleagues. Every classmate got 2 candies. In the end, Annie got left with 12 candies. If there are 35 people in Annie's class in total, how much did Annie spend on candies if one candy costs $0.1?"""
    candies_per_person = 2
    classmates = 35
    total_candies = candies_per_person * classmates - 12
    price_per_candy = 0.1
    total_cost = total_candies * price_per_candy
    result = total_cost
    return result

print(solution())