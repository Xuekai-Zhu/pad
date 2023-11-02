def solution():
    """
    Penelope the pig eats 20 pounds of food per day, which is 10 times more than Greta the goose eats per day.
    Milton the mouse eats 1/100 as much as Greta the goose eats per day, but Elmer the elephant eats 4000 times more
    than Milton the mouse does per day. How much more, in pounds, does Elmer the elephant eat per day than Penelope the pig?
    """
    penelope_daily_food = 20
    greta_daily_food = penelope_daily_food / 10
    milton_daily_food = greta_daily_food / 100
    elmer_daily_food = milton_daily_food * 4000
    difference = elmer_daily_food - penelope_daily_food
    result = difference
    return result

print(solution())