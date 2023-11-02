def solution():
    # Calculate the total amount of gold found by Jim
    total_gold = 100 + 2*(0.5*100)  # Jim finds a treasure chest with 100 gold coins and 2 smaller bags with half as much gold each
    gold_per_hour = total_gold / 8  # Jim spends 8 hours scuba diving
    result = gold_per_hour
    return result

print(solution())