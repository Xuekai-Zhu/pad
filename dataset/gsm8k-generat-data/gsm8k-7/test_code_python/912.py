def solution():
    betty_strawberries = 16
    matthew_strawberries = betty_strawberries + 20
    natalie_strawberries = matthew_strawberries / 2

    total_strawberries = betty_strawberries + matthew_strawberries + natalie_strawberries

    jars_of_jam = total_strawberries // 7

    price_per_jar = 4

    total_money = jars_of_jam * price_per_jar

    result = total_money
    return result

print(solution())