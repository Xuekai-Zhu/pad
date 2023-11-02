def solution():
    num_burritos = 10
    burrito_calories = 120
    burrito_price = 6

    num_burgers = 5
    burger_calories = 400
    burger_price = 8

    # Calculate the total number of calories per dollar for the burritos
    burrito_calories_per_dollar = (num_burritos * burrito_calories) / burrito_price

    # Calculate the total number of calories per dollar for the burgers
    burger_calories_per_dollar = (num_burgers * burger_calories) / burger_price

    # Calculate the difference in calories per dollar between the burgers and burritos
    difference = burger_calories_per_dollar - burrito_calories_per_dollar
    result = difference
    return result

print(solution())