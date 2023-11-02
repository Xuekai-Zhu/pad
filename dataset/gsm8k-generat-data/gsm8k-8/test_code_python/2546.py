def solution():
    # Calculate amount of coffee Jack can make in one batch
    batch_size = 1.5 * 128  # convert gallons to ounces

    # Calculate how many batches Jack needs to make to last 24 days
    total_coffee_needed = 96 * 12  # 96 oz every 2 days for 24 days
    batches_needed = total_coffee_needed / batch_size

    # Calculate amount of time Jack spends making coffee
    time_per_batch = 20
    total_time = time_per_batch * batches_needed

    result = total_time
    return result

print(solution())