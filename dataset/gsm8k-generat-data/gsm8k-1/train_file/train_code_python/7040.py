def solution():
    """Elida has 5 letters while Adrianna has 2 less than twice the number of letters Elida has. What's 10 times the average number of letters in both names?"""
    elida_letters = 5
    adrianna_letters = 2 * elida_letters - 2
    average_letters = (elida_letters + adrianna_letters) / 2
    result = 10 * average_letters
    return result

print(solution())