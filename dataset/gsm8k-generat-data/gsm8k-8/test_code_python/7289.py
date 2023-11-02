def solution():
    hot_dog_cost = 1.5
    salad_cost = 2.5
    num_hot_dogs = 5
    num_salads = 3
    total_cost = (hot_dog_cost * num_hot_dogs) + (salad_cost * num_salads)
    paid = 10 * 2
    change = paid - total_cost
    result = change
    return result

print(solution())