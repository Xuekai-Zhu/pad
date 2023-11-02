def solution():
    # Calculate the total number of oranges
    total_oranges = 10 * 30  # each bag has 30 oranges and there are 10 bags
    # Calculate the number of good oranges
    good_oranges = total_oranges - 50  # 50 pieces of oranges are rotten
    # Calculate the number of oranges for juice
    juice_oranges = 30  # 30 pieces of oranges will be kept for making juice
    # Calculate the number of oranges to be sold
    sold_oranges = good_oranges - juice_oranges
    result = sold_oranges
    return result

print(solution())