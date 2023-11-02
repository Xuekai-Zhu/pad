def solution():
    """In one day, Ella's dog eats 4 pounds of food for every one pound of food that Ella eats. How much food do Ella and her dog in 10 days if Ella eat 20 pounds of food each day?"""
    # Define the amount of food Ella eats each day
    ella_food_per_day = 20

    # Define the ratio of dog food to Ella's food
    dog_food_ratio = 4

    # Calculate the amount of dog food eaten each day
    dog_food_per_day = ella_food_per_day * dog_food_ratio

    # Calculate the total amount of food eaten by Ella and her dog in 10 days
    total_food = (ella_food_per_day + dog_food_per_day) * 10

    # return the result
    result = total_food
    return result

print(solution())