def solution():
    kittens = 4
    adult_cats = 3
    days = 7
    cans_of_food = 7
    adult_food = 1
    kitten_food = .75
    needed_food = ((adult_cats * adult_food) + (kittens * kitten_food))
    additional_food = (needed_food - days)
    result = additional_food
 
    return result

print(solution())