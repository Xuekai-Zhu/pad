def solution():
    squirrels_caught = 6
    rabbits_caught = 2
    calories_per_squirrel = 300
    calories_per_rabbit = 800
    total_calories_squirrels = squirrels_caught * calories_per_squirrel
    total_calories_rabbits = rabbits_caught * calories_per_rabbit
    difference = total_calories_squirrels - total_calories_rabbits
    result = difference
    return result

print(solution())