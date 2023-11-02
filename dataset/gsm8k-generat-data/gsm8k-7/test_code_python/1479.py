def solution():
    batches_needed = 6  # 60 bags / 10 bags per batch = 6 batches needed
    batches_available = 2  # 20 bags / 10 bags per batch = 2 batches available
    batches_to_make = batches_needed - batches_available

    # Assuming it takes one night to make one batch of jerky,
    # the number of days needed to make the remaining batches will be equal to the number of remaining batches
    days_needed = batches_to_make

    result = days_needed
    return result

print(solution())