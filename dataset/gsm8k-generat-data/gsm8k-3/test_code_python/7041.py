def solution():
    """Elida has 5 letters while Adrianna has 2 less than twice the number of letters Elida has. What's 10 times the average number of letters in both names?"""
    # Define the number of letters in Elida's name and calculate the number of letters in Adrianna's name
    elida_letters = 5
    adrianna_letters = 2 * elida_letters - 2

    # Calculate the average number of letters in both names and multiply by 10
    avg_letters = (elida_letters + adrianna_letters) / 2
    result = 10 * avg_letters
    return result

print(solution())