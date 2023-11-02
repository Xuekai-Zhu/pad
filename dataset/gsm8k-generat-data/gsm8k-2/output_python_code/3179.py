def solution():
    """Toby is making toast and adding peanut butter to it. He wants to make sure he has 500 calories for breakfast. A piece of bread has 100 calories. A serving of peanut butter has 200 calories. If he has one piece of bread, how many servings of peanut butter should he add?"""
    bread_calories = 100
    peanut_butter_calories = 200
    total_calories = 500
    bread_count = 1
    peanut_butter_count = (total_calories - (bread_calories * bread_count)) / peanut_butter_calories
    result = peanut_butter_count
    return result

print(solution())