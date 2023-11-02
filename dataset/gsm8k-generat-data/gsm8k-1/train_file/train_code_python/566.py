def solution():
    """Lilith originally had five dozen water bottles that she needed to sell at $2 each to get exactly enough money to buy her friend a birthday gift. However, at the store, Lilith realized she could not sell at $2 because the regular price was $1.85 per water bottle in her town, and she had to reduce her price to $1.85 as well to sell her water bottles. Calculate the total amount of money Lilith will have to find to buy her friend the birthday gift after selling her water bottles at the reduced cost."""
    dozens_of_water_bottles = 5
    water_bottles_per_dozen = 12
    total_water_bottles = dozens_of_water_bottles * water_bottles_per_dozen
    original_price = 2
    reduced_price = 1.85
    total_money = total_water_bottles * reduced_price
    amount_to_find = total_money - (original_price * total_water_bottles)
    result = amount_to_find
    return result

print(solution())