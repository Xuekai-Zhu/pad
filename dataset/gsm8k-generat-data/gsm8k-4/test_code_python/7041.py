def solution():
    """Elida has 5 letters while Adrianna has 2 less than twice the number of letters Elida has. What's 10 times the average number of letters in both names?"""
    # Define the number of letters in Elida's name
    elida_letters = 5

    # Calculate the number of letters in Adrianna's name
    adrianna_letters = 2 * elida_letters - 2

    # Calculate the average number of letters in both names
    avg_letters = (elida_letters + adrianna_letters) / 2

    # Calculate 10 times the average number of letters
    result = 10 * avg_letters
    return result

print(solution())