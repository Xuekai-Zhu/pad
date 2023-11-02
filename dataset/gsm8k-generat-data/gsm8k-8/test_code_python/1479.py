def solution():
    # Calculate the number of batches needed to fulfill the order
    total_bags = 60
    pre_made = 20
    bags_needed = total_bags - pre_made
    batches_needed = bags_needed / 10

    # Calculate the number of days needed to make the required batches
    days_per_batch = 1
    total_days = batches_needed * days_per_batch
    result = total_days
    return result

print(solution())