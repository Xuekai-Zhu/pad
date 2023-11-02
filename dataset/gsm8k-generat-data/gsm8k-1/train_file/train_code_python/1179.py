def solution():
    """A local restaurant is offering an 8 piece fried chicken bucket and 2 sides for $12.00 that will feed 6 people. If Monty was having a family reunion for 36 family members, how much will it cost him to buy enough chicken and sides to feed everyone one serving?"""
    servings_per_bucket = 6
    servings_needed = 36
    buckets_needed = servings_needed / servings_per_bucket
    cost_per_bucket = 12
    cost_per_serving = cost_per_bucket / servings_per_bucket
    cost_per_person = cost_per_serving * 2
    total_cost = cost_per_person * servings_needed
    result = total_cost
    return result

print(solution())