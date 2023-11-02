def solution():
    batch_size = 1.5 * 128  # 1.5 gallons converted to ounces
    coffee_consumed = 96  # Jack drinks 96 ounces of coffee every 2 days
    time_per_batch = 20  # It takes Jack 20 hours to make one batch of coffee
    days = 24  # Jack wants to know how long he will spend making coffee over 24 days

    # Calculate the number of batches Jack will make in 24 days
    num_batches = (coffee_consumed * days) / batch_size

    # Calculate the total time Jack will spend making coffee in 24 days
    total_time = num_batches * time_per_batch
    result = total_time
    return result

print(solution())