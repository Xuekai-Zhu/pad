def solution():
    """Penelope the pig eats 20 pounds of food per day, which is 10 times more than Greta the goose eats per day.  Milton the mouse eats 1/100 as much as Greta the goose eats per day, but Elmer the elephant eats 4000 times more than Milton the mouse does per day.  How much more, in pounds, does Elmer the elephant eat per day than Penelope the pig?"""
    # Define the daily food intake for each animal
    pig_daily_food = 20
    goose_daily_food = pig_daily_food / 10
    mouse_daily_food = goose_daily_food / 100
    elephant_daily_food = mouse_daily_food * 4000

    # Calculate the difference in daily food intake between the elephant and the pig
    food_difference = elephant_daily_food - pig_daily_food

    # Display the difference in daily food intake between the elephant and the pig
    result = food_difference
    return result

print(solution())