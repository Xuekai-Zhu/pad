def solution():
    initial_money = 20
    book1_cost = 8
    book2_cost = 4
    poster_cost = 4

    # Calculate the amount of money left after buying the first two books
    money_left = initial_money - book1_cost - book2_cost

    # Calculate the maximum number of posters that can be bought with the money left
    num_posters = money_left // poster_cost
    result = num_posters
    return result

print(solution())