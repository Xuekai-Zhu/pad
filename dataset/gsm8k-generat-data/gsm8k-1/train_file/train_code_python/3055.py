def solution():
    """My cat's empty bowl weighs 420 grams. If I give my cat 60 grams per day and I always fill her bowl every 3 days, how much does her bowl weigh if after I ended up refilling her empty bowl she only ate 14 grams?"""
    empty_bowl_weight = 420
    daily_cat_food_amount = 60
    refill_days = 3
    total_food_amount = daily_cat_food_amount * refill_days
    remaining_food = total_food_amount - 14
    new_bowl_weight = empty_bowl_weight + remaining_food
    result = new_bowl_weight
    return result

print(solution())