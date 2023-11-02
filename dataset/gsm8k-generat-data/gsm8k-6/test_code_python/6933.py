def solution():
    # Calculate the total pounds of ground mince used in lasagnas
    lasagnas_minced = 100 * 2

    # Calculate the remaining pounds of ground mince available for cottage pies
    cottage_pies_minced = 500 - lasagnas_minced

    # Calculate the number of cottage pies that can be made with the remaining ground mince
    cottage_pies = cottage_pies_minced // 3
    result = cottage_pies
    return result

print(solution())