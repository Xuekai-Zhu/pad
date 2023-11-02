def solution():
    """Penelope the pig eats 20 pounds of food per day, which is 10 times more than Greta the goose eats per day. Milton the mouse eats 1/100 as much as Greta the goose eats per day, but Elmer the elephant eats 4000 times more than Milton the mouse does per day. How much more, in pounds, does Elmer the elephant eat per day than Penelope the pig?"""
    greta_eats = 20 / 10
    milton_eats = greta_eats / 100
    elmer_eats = milton_eats * 4000
    difference = elmer_eats - 20
    result = difference
    return result

print(solution())