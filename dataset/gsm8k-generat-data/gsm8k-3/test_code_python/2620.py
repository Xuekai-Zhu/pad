def solution():
    """Ryan started with 36 tokens at the arcade. Ryan wasted a third of his tokens on Pac-Man, a fourth of his tokens on Candy Crush, and 7 on Ski-ball. Then, his parents bought him seven times as many tokens as he spent on Ski-ball. How many tokens did Ryan end up with?"""
    # Define the number of starting tokens
    starting_tokens = 36

    # Calculate the number of tokens spent on Pac-Man
    pacman_tokens = starting_tokens / 3

    # Calculate the number of tokens spent on Candy Crush
    candy_tokens = starting_tokens / 4

    # Calculate the number of tokens spent on Ski-ball
    ski_tokens = 7

    # Calculate the number of tokens Ryan's parents bought for him
    parent_tokens = ski_tokens * 7

    # Calculate the total number of tokens Ryan ended up with
    total_tokens = starting_tokens - pacman_tokens - candy_tokens - ski_tokens + parent_tokens

    # Display the total number of tokens
    result = total_tokens
    return result

print(solution())