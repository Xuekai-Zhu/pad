def solution():
    ella_food_per_day = 20  # Ella eats 20 pounds of food per day
    ella_food_total = ella_food_per_day * 10  # Ella eats 20 pounds of food per day for 10 days

    dog_food_total = 4 * ella_food_total  # The dog eats 4 pounds of food for every 1 pound of food Ella eats
    total_food = ella_food_total + dog_food_total

    result = total_food
    return result

print(solution())