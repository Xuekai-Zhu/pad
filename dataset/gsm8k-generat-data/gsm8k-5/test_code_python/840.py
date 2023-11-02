def solution():
    # Calculate the total amount of food ate by the dogs in a day
    food_per_day_dog = 4 * 3 * 2  # 4 pounds of food, 3 times a day, 2 times the amount of puppies
    total_food_dogs = food_per_day_dog * 3  # Three dogs eat this amount of food per day

    # Calculate the total amount of food ate by the puppies in a day
    food_per_day_puppy = food_per_day_dog / 2  # Each dog eats twice as much as a puppy
    total_food_puppies = food_per_day_puppy * 3 * 4  # Four puppies eat this amount of food per day, eating three times as often as a dog

    # Calculate the total amount of food ate by all the dogs and puppies
    total_food = total_food_dogs + total_food_puppies
    result = total_food
    return result

print(solution())