def solution():
    # Convert total pounds of eggs needed to ounces
    total_ounces = 6 * 16

    # Calculate the total number of eggs needed
    total_eggs = total_ounces / (1/16)

    # Calculate the number of dozens of eggs needed
    dozens_of_eggs = total_eggs / 12

    result = dozens_of_eggs
    return result

print(solution())