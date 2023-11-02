def solution():
    num_dogs = 4  # Aunt Gemma has four dogs
    food_per_dog_per_meal = 250  # Each dog can consume 250 grams of food per meal
    meals_per_day = 2  # Aunt Gemma feeds her dogs twice a day
    total_food_per_day = num_dogs * food_per_dog_per_meal * meals_per_day / 1000  # Convert grams to kilograms

    # Calculate how many days the food will last based on the amount of food bought
    total_food_bought = 2 * 50  # Aunt Gemma bought 2 sacks of dog food, each weighing 50 kilograms
    days_worth_of_food = total_food_bought / total_food_per_day
    result = days_worth_of_food
    return result

print(solution())