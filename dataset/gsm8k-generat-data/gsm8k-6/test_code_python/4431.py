def solution():
    # Determine the number of bell peppers Jaylen has
    bell_peppers = 2 * 2  # Jaylen has twice as many bell peppers as Kristin

    # Determine the number of green beans Jaylen has
    green_beans = (1/2) * 20 - 3  # Jaylen has 3 less than half as many green beans as Kristin

    # Determine the total number of vegetables Jaylen has
    total_vegetables = 5 + 2 + bell_peppers + green_beans

    result = total_vegetables
    return result

print(solution())