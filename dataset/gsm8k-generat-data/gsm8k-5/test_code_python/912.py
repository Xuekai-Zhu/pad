def solution():
    betty_strawberries = 16
    matthew_strawberries = betty_strawberries + 20
    natalie_strawberries = betty_strawberries / 2
    total_strawberries = betty_strawberries + matthew_strawberries + natalie_strawberries

    # Calculate the number of jars of jam they made
    jars_of_jam = total_strawberries // 7

    # Calculate the total money made from selling the jars of jam
    total_money = jars_of_jam * 4
    result = total_money
    return result

print(solution())