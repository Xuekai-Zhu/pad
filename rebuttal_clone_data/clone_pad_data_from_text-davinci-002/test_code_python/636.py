def solution():
    sticky_keys = 15
    minutes_per_key = 3
    keys_left = sticky_keys - 1
    minutes_to_clean = keys_left * minutes_per_key
    minutes_to_assign = 10
    total_minutes = minutes_to_clean + minutes_to_assign
    result = total_minutes
    return result

Question: At Joe's pizzeria a pizza costs $5 with the first topping, and then an additional 75 cents for each additional topping. If Tommy wants a pizza with mushrooms, onions, and green peppers, how much will his pizza cost?
Solution:
def solution():
    base_price = 5
    topping_price = 0.75
    number_of_toppings = 3
    total_price = base_price + (number_of_toppings * topping_price)
    result = total_price
    return result

print(solution())