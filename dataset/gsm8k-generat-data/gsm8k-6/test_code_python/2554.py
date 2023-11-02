def solution():
    small_price = 1.5  # price of a small apple
    medium_price = 2  # price of a medium apple
    big_price = 3  # price of a big apple
    num_small = 6  # number of small apples bought by Donny
    num_medium = 6  # number of medium apples bought by Donny
    num_big = 8  # number of big apples bought by Donny

    # Calculate the total cost of the apples bought by Donny
    total_cost = (num_small * small_price) + (num_medium * medium_price) + (num_big * big_price)
    result = total_cost
    return result

print(solution())