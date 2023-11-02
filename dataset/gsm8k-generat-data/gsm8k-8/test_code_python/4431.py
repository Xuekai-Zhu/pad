def solution():
    # Define the number of vegetables Kristin has
    kristin_bell_peppers = 2
    kristin_green_beans = 20

    # Calculate the number of bell peppers Jaylen has
    jaylen_bell_peppers = kristin_bell_peppers * 2

    # Calculate the number of green beans Jaylen has
    jaylen_green_beans = (0.5 * kristin_green_beans) - 3

    # Calculate the total number of vegetables Jaylen has
    total_vegetables = jaylen_bell_peppers + jaylen_green_beans + 5 + 2

    result = total_vegetables
    return result

print(solution())