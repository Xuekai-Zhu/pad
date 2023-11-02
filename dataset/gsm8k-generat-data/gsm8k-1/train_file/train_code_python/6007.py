def solution():
    """Tom catches crabs for a living. He has 8 crab buckets that he checks every day. Each crab bucket gets 12 crabs. He sells each of these crabs for $5 each. How much money does he make per week?"""
    crab_buckets = 8
    crabs_per_bucket = 12
    price_per_crab = 5
    crabs_caught_per_week = crab_buckets * crabs_per_bucket * 7
    money_made = crabs_caught_per_week * price_per_crab
    result = money_made
    return result

print(solution())