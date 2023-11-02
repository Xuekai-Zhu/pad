def solution():
    num_guests = 30
    num_burgers = num_guests * 1.5  # 1.5 burgers per guest
    burgers_per_batch = 5
    time_per_batch = 8  # 4 minutes per side, 2 sides per burger
    num_batches = num_burgers / burgers_per_batch
    total_time = num_batches * time_per_batch
    result = total_time
    return result

print(solution())