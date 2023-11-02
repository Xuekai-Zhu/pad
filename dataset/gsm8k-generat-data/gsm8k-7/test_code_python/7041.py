def solution():
    elida_letters = 5
    adrianna_letters = 2 * elida_letters - 2

    # Calculate the average number of letters in both names
    avg_letters = (elida_letters + adrianna_letters) / 2

    # Calculate 10 times the average number of letters
    result = 10 * avg_letters
    return result

print(solution())