def solution():
    betty_strawberries = 16
    matthew_strawberries = betty_strawberries + 20
    natalie_strawberries = betty_strawberries / 2
    total_strawberries = betty_strawberries + matthew_strawberries + natalie_strawberries
    total_jars = total_strawberries / 7
    total_money = total_jars * 4
    result = total_money
    return result

print(solution())