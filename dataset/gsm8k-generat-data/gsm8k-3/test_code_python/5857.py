def solution():
    """In one day, Ella's dog eats 4 pounds of food for every one pound of food that Ella eats. How much food do Ella and her dog in 10 days if Ella eat 20 pounds of food each day?"""
    # Define the ratio of Ella's dog's food to Ella's food
    DOG_FOOD_RATIO = 4

    # Define the amount of food Ella eats per day
    ella_food = 20

    # Calculate the amount of food Ella's dog eats per day
    dog_food = DOG_FOOD_RATIO * ella_food

    # Calculate the total amount of food eaten by Ella and her dog in 10 days
    total_food = (ella_food + dog_food) * 10

    # Display the total amount of food
    result = total_food
    return result

print(solution())