def solution():
    # Calculate the total amount of mince used for the lasagnas
    lasagna_mince = 100 * 2

    # Calculate the remaining amount of mince available for the cottage pies
    cottage_mince = 500 - lasagna_mince

    # Calculate the number of cottage pies that can be made with the remaining mince
    cottage_pies = cottage_mince // 3
    result = cottage_pies
    return result

print(solution())