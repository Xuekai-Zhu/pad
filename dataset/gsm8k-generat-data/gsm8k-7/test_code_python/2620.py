def solution():
    starting_tokens = 36

    # Calculate the number of tokens spent on Pac-Man
    pacman_tokens = starting_tokens / 3

    # Calculate the number of tokens spent on Candy Crush
    candy_tokens = starting_tokens / 4

    # Calculate the total number of tokens spent
    total_spent = pacman_tokens + candy_tokens + 7

    # Calculate the number of tokens Ryan's parents bought him
    new_tokens = 7 * total_spent

    # Calculate the total number of tokens Ryan now has
    total_tokens = starting_tokens - total_spent + new_tokens
    result = total_tokens
    return result

print(solution())