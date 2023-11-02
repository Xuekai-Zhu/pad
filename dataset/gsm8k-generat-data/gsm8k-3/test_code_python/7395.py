def solution():
    """Matilda has half as many jellybeans as Matt. Matt has ten times as many jellybeans as Steve. If Steve has 84 jellybeans, how many jellybeans does Matilda have?"""
    # Define the number of jellybeans Steve has
    steve_jellybeans = 84

    # Calculate the number of jellybeans Matt has
    matt_jellybeans = steve_jellybeans * 10

    # Calculate the number of jellybeans Matilda has
    matilda_jellybeans = matt_jellybeans / 2

    # Display the number of jellybeans Matilda has
    result = matilda_jellybeans
    return result

print(solution())