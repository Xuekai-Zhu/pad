def solution():
    # Calculate the number of strawberries Matthew picked
    matthew_picked = 16 + 20 + 2 * (16)

    # Calculate the total number of strawberries picked
    total_strawberries = 16 + matthew_picked + (matthew_picked / 2)

    # Calculate the number of jars of jam they can make
    jars_of_jam = total_strawberries / 7

    # Calculate the total money they made from the jam
    total_money = jars_of_jam * 4

    result = total_money
    return result

print(solution())