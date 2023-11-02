def solution():
    # Calculate the number of chocolates Matilda and her 4 sisters each received
    chocolates_each = 20 / 5  

    # Calculate the total number of chocolates surrendered by Matilda and her sisters to their father
    surrendered_chocolates = (1/2) * 20  

    # Calculate the number of chocolates left with the father
    remaining_chocolates = surrendered_chocolates - 2  # father ate 2 chocolates, gave 3 to mother
    result = remaining_chocolates
    return result

print(solution())