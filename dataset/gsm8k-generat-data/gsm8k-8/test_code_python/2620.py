def solution():
    # Define the starting number of tokens
    starting_tokens = 36

    # Calculate the number of tokens spent on Pac-Man and Candy Crush
    pac_man_tokens = starting_tokens / 3
    candy_crush_tokens = starting_tokens / 4

    # Calculate the number of tokens spent in total
    total_tokens_spent = pac_man_tokens + candy_crush_tokens + 7

    # Calculate the number of tokens Ryan's parents bought for him
    parent_tokens = 7 * total_tokens_spent

    # Calculate the total number of tokens Ryan ends up with
    end_tokens = starting_tokens - total_tokens_spent + parent_tokens
    result = end_tokens
    return result

print(solution())