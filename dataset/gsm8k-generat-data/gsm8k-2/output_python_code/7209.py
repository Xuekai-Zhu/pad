def solution():
    """Peter is eating chips. Each chip is 10 calories. A bag has 24 chips and costs $2. If he wants to eat 480 calories, how much does he have to spend on chips?"""
    calories_per_chip = 10
    chips_per_bag = 24
    bag_price = 2
    calories_needed = 480
    chips_needed = calories_needed / calories_per_chip
    bags_needed = chips_needed / chips_per_bag
    total_cost = bags_needed * bag_price
    result = total_cost
    return result

print(solution())