def solution():
     calories_from_sugar = 150
     percent_sugar = 5
     calories_from_drink = 2500
     sugar_calories_drink = (calories_from_drink * percent_sugar) / 100
     candy_calories = 25
     number_of_candy = (calories_from_sugar + (sugar_calories_drink - calories_from_sugar)) / candy_calories
     result = number_of_candy
     return result

print(solution())