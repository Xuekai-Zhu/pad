def solution():
    # Define the number of chickens each person has
    q_chickens = 2 * s_chickens + 25
    s_chickens = 3 * c_chickens - 4

    # Calculate the total number of chickens
    total_chickens = q_chickens + s_chickens + c_chickens
    c_chickens = (383 - q_chickens - s_chickens) / 3

    result = c_chickens
    return result

print(solution())