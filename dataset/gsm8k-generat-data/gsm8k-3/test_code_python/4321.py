def solution():
    """Tino has 24 more jellybeans than Lee. Arnold has half as many jellybeans as Lee. If Arnold has 5 jellybeans, how many jellybeans does Tino have?"""
    # Define the number of jellybeans Arnold has
    arnold_jellybeans = 5

    # Calculate the number of jellybeans Lee has
    lee_jellybeans = arnold_jellybeans * 2

    # Calculate the number of jellybeans Tino has
    tino_jellybeans = lee_jellybeans + 24

    # Display the number of jellybeans Tino has
    result = tino_jellybeans
    return result

print(solution())