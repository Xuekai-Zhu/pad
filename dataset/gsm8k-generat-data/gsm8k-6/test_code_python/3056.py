def solution():
    # Calculate the weight of the food my cat ate in 3 days
    food_per_3_days = 60 * 3  # my cat eats 60 grams per day and I fill her bowl every 3 days
    remaining_food = food_per_3_days - 14  # my cat only ate 14 grams of the food I gave her
    empty_bowl = 420  # the weight of the empty bowl is 420 grams
    bowl_with_remaining_food = empty_bowl + remaining_food  # calculate the weight of the bowl with remaining food
    result = bowl_with_remaining_food
    return result

print(solution())