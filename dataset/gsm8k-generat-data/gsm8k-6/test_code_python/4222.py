def solution():
    # Calculate the total number of fruits in the three baskets
    total_fruits = 58 - 18 - 10 - 12  # subtract the number of fruits in the first 3 baskets from the total number of fruits
    # Calculate the number of fruits in each of the remaining two baskets
    kiwi_lemon = total_fruits // 2  # divide the total number of fruits by 2, since there are two baskets with the same number of fruits
    # Calculate the number of lemons in one of the baskets
    lemons = kiwi_lemon // 2  # divide the number of fruits in one of the baskets by 2, since it contains both kiwi and lemon
    result = lemons
    return result

print(solution())