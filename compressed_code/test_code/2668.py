def solution():
    
    burrito_price = 6
    burrito_calories = 120
    burger_price = 8
    burger_calories = 400
    burrito_calories_per_dollar = (10 * burrito_calories) / burrito_price
    burger_calories_per_dollar = (5 * burger_calories) / burger_price
    difference = burger_calories_per_dollar - burrito_calories_per_dollar
    result = difference
    return result

print(solution())