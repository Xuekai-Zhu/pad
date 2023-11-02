def solution():
    mom_food = 1.5
    puppies_food = 0.5
    number_of_puppies = 5
    total_food = ((mom_food * 3) + ((puppies_food * 2) * number_of_puppies)) * 6
    result = total_food
    return result

print(solution())