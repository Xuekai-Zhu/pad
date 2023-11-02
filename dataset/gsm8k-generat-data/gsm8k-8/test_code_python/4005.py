def solution():
    # Define the total amount of money Shelby has
    total_money = 20

    # Deduct the cost of the two books
    total_money -= 8  # Cost of book 1
    total_money -= 4  # Cost of book 2

    # Calculate the number of $4 posters she can buy with the remaining money
    num_posters = total_money // 4
    result = num_posters
    return result

print(solution())