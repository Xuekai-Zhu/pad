def solution():
    """Tom catches crabs for a living. He has 8 crab buckets that he checks every day. Each crab bucket gets 12 crabs. He sells each of these crabs for $5 each. How much money does he make per week?"""
    buckets_per_day = 8
    crabs_per_bucket = 12
    crabs_per_day = buckets_per_day * crabs_per_bucket
    price_per_crab = 5
    income_per_day = crabs_per_day * price_per_crab
    income_per_week = income_per_day * 7
    result = income_per_week
    return result

print(solution())