def solution():
    # Define the daily food intake of Penelope and Greta
    penelope_daily_food = 20
    greta_daily_food = penelope_daily_food / 10

    # Define the daily food intake of Milton and Elmer
    milton_daily_food = greta_daily_food / 100
    elmer_daily_food = milton_daily_food * 4000

    # Calculate how much more Elmer eats than Penelope
    food_diff = elmer_daily_food - penelope_daily_food
    result = food_diff
    return result

print(solution())