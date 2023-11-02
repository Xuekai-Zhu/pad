def solution():
    """In one day, Ella's dog eats 4 pounds of food for every one pound of food that Ella eats. How much food do Ella and her dog in 10 days if Ella eat 20 pounds of food each day?"""
    ella_food_per_day = 20
    dog_food_per_day = 4 * ella_food_per_day
    total_food_per_day = ella_food_per_day + dog_food_per_day
    total_food_10_days = total_food_per_day * 10
    result = total_food_10_days
    return result

print(solution())