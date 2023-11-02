def solution():
    ella_food = 20 * 10  # Ella eats 20 pounds of food per day for 10 days
    dog_food = ella_food * 4  # Ella's dog eats 4 pounds of food for every 1 pound of food that Ella eats
    total_food = ella_food + dog_food  # total amount of food eaten in 10 days

    result = total_food
    return result

print(solution())