def solution():
    num_eggs = 30
    cost = 5.0
    selling_price = 0.2

    # Calculate the total revenue Samantha will earn by selling all the eggs
    total_revenue = num_eggs * selling_price

    # Calculate the number of eggs she needs to sell to recover her capital
    num_eggs_to_sell = cost / selling_price

    # Calculate the number of eggs she will have left after selling enough to recover her capital
    num_eggs_left = num_eggs - num_eggs_to_sell
    result = num_eggs_left
    return result

print(solution())