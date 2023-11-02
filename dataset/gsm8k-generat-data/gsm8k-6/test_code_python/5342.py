def solution():
    # Find the number of chocolates Alix initially hides
    alix_chocolates = 3 * 10  

    # Find the number of chocolates Alix has after Mom takes 5 chocolates
    alix_chocolates_left = alix_chocolates - 5  

    # Find the difference between Alix and Nick's chocolates
    difference = alix_chocolates_left - 10 

    result = difference
    return result

print(solution())