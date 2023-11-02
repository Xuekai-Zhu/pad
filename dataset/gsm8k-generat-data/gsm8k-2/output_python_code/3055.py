def solution():
    """My cat's empty bowl weighs 420 grams. If I give my cat 60 grams per day and I always fill her bowl every 3 days, how much does her bowl weigh if after I ended up refilling her empty bowl she only ate 14 grams?"""
    empty_bowl_weight = 420
    food_per_day = 60
    days_between_refills = 3
    food_per_refill = food_per_day * days_between_refills
    total_food_eaten = food_per_refill - 14
    new_bowl_weight = empty_bowl_weight + total_food_eaten
    result = new_bowl_weight
    return result

print(solution())