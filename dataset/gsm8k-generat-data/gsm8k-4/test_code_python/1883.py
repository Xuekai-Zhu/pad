def solution():
    """Jim spends 8 hours scuba diving. In that time he finds a treasure chest with 100 gold coins in it. He also finds 2 smaller bags that have half as much gold each. How much gold does he find per hour?"""
    # Define the number of hours Jim spends scuba diving
    hours_diving = 8

    # Define the number of gold coins in the treasure chest
    treasure_chest_gold = 100

    # Define the amount of gold in each smaller bag
    small_bag_gold = treasure_chest_gold / 2

    # Calculate the total amount of gold Jim finds
    total_gold = treasure_chest_gold + (2 * small_bag_gold)

    # Calculate the amount of gold Jim finds per hour
    gold_per_hour = total_gold / hours_diving

    # Return the result
    result = gold_per_hour
    return result

print(solution())