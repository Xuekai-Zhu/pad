def solution():
    """John runs a telethon to raise money. For the first 12 hours, he generates $5000 per hour. The remaining 14 hours, he generates 20% more per hour. How much total money does he make?"""
    # Define the hourly rate for the first 12 hours
    first_12_rate = 5000

    # Calculate the total money raised in the first 12 hours
    first_12_total = first_12_rate * 12

    # Calculate the hourly rate for the remaining 14 hours
    remaining_rate = first_12_rate * 1.2

    # Calculate the total money raised in the remaining 14 hours
    remaining_total = remaining_rate * 14

    # Calculate the total money raised for the entire telethon
    total_money = first_12_total + remaining_total

    result = total_money
    return result

print(solution())