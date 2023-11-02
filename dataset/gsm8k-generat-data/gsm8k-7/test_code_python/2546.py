def solution():
    batch_size = 1.5 * 128  # 1.5 gallons to ounces
    coffee_consumption_rate = 96  # ounces every 2 days
    coffee_making_time = 20  # hours
    num_days = 24

    # Calculate the total coffee consumed over 24 days
    total_coffee_consumed = (num_days * 24) / 2 * coffee_consumption_rate

    # Calculate the total number of batches needed
    total_batches = total_coffee_consumed / batch_size

    # Calculate the total time spent making coffee
    total_time = total_batches * coffee_making_time

    result = total_time
    return result

print(solution())