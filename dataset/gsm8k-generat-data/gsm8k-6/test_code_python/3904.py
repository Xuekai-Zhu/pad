def solution():
    # Calculate the total cost of the folders and pencils
    total_folders_cost = 6 * 6  # 1 folder for each of 6 classes, and each folder costs $6
    total_pencils_cost = 6 * 3 * 2  # 3 pencils for each of 6 classes, and each pencil costs $2

    # Calculate the number of erasers needed and the total erasers cost
    total_erasers_needed = total_pencils_cost // 6
    total_erasers_cost = total_erasers_needed * 1  # 1 eraser for every 6 pencils, and each eraser costs $1

    # Calculate the remaining amount of money for the paints
    remaining_money = 80 - total_folders_cost - total_pencils_cost - total_erasers_cost
    paints_cost = remaining_money  # The remaining amount of money is spent on the set of paints

    result = paints_cost
    return result

print(solution())