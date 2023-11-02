def solution():
    # Find the number of tokens Ryan spent on Pac-Man
    pac_man_tokens = 36 / 3

    # Find the number of tokens Ryan spent on Candy Crush
    candy_crush_tokens = 36 / 4

    # Find the total number of tokens Ryan spent
    total_spent = pac_man_tokens + candy_crush_tokens + 7

    # Find the number of tokens Ryan's parents bought him
    parents_tokens = 7 * total_spent

    # Find the total number of tokens Ryan has now
    total_tokens = 36 - total_spent + parents_tokens

    result = total_tokens
    return result

print(solution())