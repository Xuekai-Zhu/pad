def solution():
    # Calculate the total number of flowers planted
    total_planted = 2 * (5 + 20) - 10  # 2 daughters plant 5 flowers each, then flowers grow by 20 but 10 die
    flowers_per_basket = total_planted / 5  # divide the total flowers by the number of baskets
    result = flowers_per_basket
    return result

print(solution())