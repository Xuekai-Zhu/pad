def solution():
    """Ryan started with 36 tokens at the arcade. Ryan wasted a third of his tokens on Pac-Man, a fourth of his tokens on Candy Crush, and 7 on Ski-ball. Then, his parents bought him seven times as many tokens as he spent on Ski-ball. How many tokens did Ryan end up with?"""
    # Define the initial number of tokens
    initial_tokens = 36

    # Calculate the number of tokens spent on Pac-Man
    pacman_tokens = initial_tokens / 3

    # Calculate the number of tokens remaining after playing Pac-Man
    remaining_tokens = initial_tokens - pacman_tokens

    # Calculate the number of tokens spent on Candy Crush
    candycrush_tokens = remaining_tokens / 4

    # Calculate the number of tokens remaining after playing Candy Crush
    remaining_tokens -= candycrush_tokens

    # Calculate the number of tokens spent on Ski-ball
    skiball_tokens = 7

    # Calculate the number of tokens Ryan's parents bought him
    parents_tokens = skiball_tokens * 7

    # Calculate the total number of tokens Ryan has now
    total_tokens = remaining_tokens + skiball_tokens + parents_tokens

    # return the result
    result = total_tokens
    return result

print(solution())