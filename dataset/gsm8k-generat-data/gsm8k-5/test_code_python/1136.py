def solution():
    dogs = 4  # Emily has 4 dogs in her home
    food_per_dog = 0.25  # Each dog eats 250 grams of food per day
    days = 14  # Emily will be on vacation for 14 days

    # Calculate the total amount of food required for all dogs during the vacation
    total_food = dogs * food_per_dog * days

    # Convert the total amount of food from grams to kilograms
    total_food_kg = total_food / 1000
    result = total_food_kg
    return result

print(solution())