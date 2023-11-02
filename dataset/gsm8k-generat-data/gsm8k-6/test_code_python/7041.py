def solution():
    # Calculate the number of letters Adrianna has
    elida_letters = 5
    adrianna_letters = 2 * elida_letters - 2

    # Find the average number of letters in both names and multiply by 10
    average_letters = (elida_letters + adrianna_letters) / 2
    result = 10 * average_letters
    return result

print(solution())