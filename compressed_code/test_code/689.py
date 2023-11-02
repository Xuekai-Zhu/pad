def solution():
    
    betty_strawberries = 16
    matthew_strawberries = betty_strawberries + 20
    natalie_strawberries = matthew_strawberries / 2
    total_strawberries = betty_strawberries + matthew_strawberries + natalie_strawberries
    jars_of_jam = total_strawberries // 7
    money_made = jars_of_jam * 4
    result = money_made
    return result

print(solution())