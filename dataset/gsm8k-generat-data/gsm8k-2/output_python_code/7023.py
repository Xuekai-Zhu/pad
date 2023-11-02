def solution():
    """Vicente bought 5 kilograms of rice and 3 pounds of meat. Each kilogram of rice is $2 and a pound of meat is $5. How much did Vicente spend in total?"""
    rice_price = 2
    meat_price = 5
    rice_weight = 5
    meat_weight = 3
    total_price = (rice_price * rice_weight) + (meat_price * meat_weight)
    result = total_price
    return result

print(solution())