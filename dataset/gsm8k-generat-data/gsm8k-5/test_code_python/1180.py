def solution():
    servings_per_bucket = 6  # An 8-piece chicken bucket with 2 sides can feed 6 people
    servings_needed = 36  # Monty needs to feed 36 family members
    buckets_needed = servings_needed / servings_per_bucket  # Calculate the number of chicken buckets needed

    # Round up the number of buckets needed to the nearest integer
    buckets_needed = math.ceil(buckets_needed)

    # Calculate the total cost of the chicken and sides
    total_cost = buckets_needed * 12.0  # Each chicken bucket with 2 sides costs $12.0
    result = total_cost
    return result

print(solution())