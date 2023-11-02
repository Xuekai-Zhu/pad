def solution():
    # Calculate how much money is left after buying the two books
    remaining_money = 20 - 8 - 4  # $8 for one book and $4 for another book
    
    # Calculate the number of posters Shelby can buy with the remaining money
    posters = remaining_money // 4
    
    result = posters
    return result

print(solution())