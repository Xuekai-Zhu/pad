def solution():
    num_people = 36
    servings_per_person = 1
    servings_per_bucket = 6
    cost_per_bucket = 12.0

    # Calculate the total number of servings needed
    total_servings = num_people * servings_per_person

    # Calculate the total number of buckets needed
    total_buckets = total_servings // servings_per_bucket

    # Calculate the total cost of all buckets
    total_cost = total_buckets * cost_per_bucket
    result = total_cost
    return result

print(solution())