def solution():
    """Penelope the pig eats 20 pounds of food per day, which is 10 times more than Greta the goose eats per day. Milton the mouse eats 1/100 as much as Greta the goose eats per day, but Elmer the elephant eats 4000 times more than Milton the mouse does per day. How much more, in pounds, does Elmer the elephant eat per day than Penelope the pig?"""
    # Calculate Greta's daily food intake
    greta_food = 20 / 10

    # Calculate Milton's daily food intake
    milton_food = greta_food * (1 / 100)

    # Calculate Elmer's daily food intake
    elmer_food = milton_food * 4000

    # Calculate the difference between Elmer's and Penelope's daily food intake
    difference = elmer_food - 20

    result = difference
    return result

print(solution())