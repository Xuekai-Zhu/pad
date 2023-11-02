def solution():
    
    price_per_can = 0.25
    cans_at_home = 12
    cans_at_grandparents = 3*cans_at_home
    cans_from_neighbor = 46
    cans_from_dad = 250
    total_cans = cans_at_home + cans_at_grandparents + cans_from_neighbor + cans_from_dad
    total_money = total_cans * price_per_can
    savings = total_money/2
    result = savings
    return result

print(solution())