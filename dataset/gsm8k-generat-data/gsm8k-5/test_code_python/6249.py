def solution():
    comics_cost = 4  # The cost of one comic is $4
    num_comics = 8  # Raul bought 8 comics
    total_cost = comics_cost * num_comics  # Calculate the total cost of the comics

    remaining_money = 87 - total_cost  # Calculate how much money Raul has left
    result = remaining_money
    return result

print(solution())