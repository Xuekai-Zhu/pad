def solution():
    elida_letters = 5  # Elida has 5 letters
    adrianna_letters = 2 * elida_letters - 2  # Adrianna has 2 less than twice the number of letters Elida has
    average_letters = (elida_letters + adrianna_letters) / 2  # Calculate the average number of letters
    ten_times_average = 10 * average_letters  # Calculate 10 times the average number of letters
    result = ten_times_average
    return result

print(solution())