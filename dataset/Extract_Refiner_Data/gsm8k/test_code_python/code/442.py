def solution():
    
    # Define the number of eggs used in cases
    eggs_in_cases = 4 * 12

    # Define the number of eggs used in the cupboard
    eggs_in_cupboard = 2

    # Calculate the total number of eggs used
    total_eggs = eggs_in_cases + eggs_in_cupboard

    # Calculate the number of trays that can be made
    trays = total_eggs // 5

    # return the result
    result = trays
    return result

print(solution())