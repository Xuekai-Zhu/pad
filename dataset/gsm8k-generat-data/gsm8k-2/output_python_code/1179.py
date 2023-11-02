def solution():
    """A local restaurant is offering an 8 piece fried chicken bucket and 2 sides for $12.00 that will feed 6 people. If Monty was having a family reunion for 36 family members, how much will it cost him to buy enough chicken and sides to feed everyone one serving?"""
    servings_needed = 36
    servings_per_bucket = 6
    buckets_needed = servings_needed / servings_per_bucket
    cost_per_bucket = 12
    cost_per_serving = cost_per_bucket / servings_per_bucket
    sides_per_bucket = 2
    total_sides_needed = buckets_needed * sides_per_bucket
    total_cost = (cost_per_bucket * buckets_needed) + (total_sides_needed * cost_per_serving)
    result = total_cost
    return result

print(solution())