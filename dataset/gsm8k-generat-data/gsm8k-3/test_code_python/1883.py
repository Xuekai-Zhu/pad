def solution():
    """Jim spends 8 hours scuba diving. In that time he finds a treasure chest with 100 gold coins in it. He also finds 2 smaller bags that have half as much gold each. How much gold does he find per hour?"""
    # Calculate the total amount of gold Jim found
    total_gold = 100 + 2 * 0.5 * 100

    # Calculate the amount of gold Jim found per hour
    gold_per_hour = total_gold / 8

    # Display the amount of gold Jim found per hour
    result = gold_per_hour
    return result

print(solution())