def solution():
    # Start with 3 bags of chocolates
    bags_of_chocolates = 3

    # Give 2 bags to siblings
    bags_of_chocolates -= 2

    # Buy 3 more bags
    bags_of_chocolates += 3

    result = bags_of_chocolates
    return result

print(solution())