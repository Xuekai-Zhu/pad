def solution():
    """Carol spends five hours filling up her pool. During the first hour, the pool fills at a rate of 8 gallons of water per hour. For the next two hours, the pool fills at 10 gallons of water per hour. For the fourth hour, the pool fills at a rate of 14 gallons of water per hour. During the fifth hour, the pool develops a leak and loses 8 gallons of water. At the end of five hours, how many gallons of water are still left in the pool?"""
    # Calculate the total amount of water added in the first hour
    first_hour = 8

    # Calculate the total amount of water added in the next two hours
    next_two_hours = 10 * 2

    # Calculate the total amount of water added in the fourth hour
    fourth_hour = 14

    # Calculate the total amount of water added in the first four hours
    total_before_leak = first_hour + next_two_hours + fourth_hour

    # Subtract the amount of water lost due to the leak
    total_after_leak = total_before_leak - 8

    # Display the total amount of water left in the pool
    result = total_after_leak
    return result

print(solution())