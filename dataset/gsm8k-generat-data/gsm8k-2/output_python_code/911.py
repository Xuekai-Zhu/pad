def solution():
    """Betty picked 16 strawberries. Matthew picked 20 more strawberries than Betty and twice as many as Natalie. They used their strawberries to make jam. One jar of jam used 7 strawberries and they sold each jar at $4. How much money were they able to make from the strawberries they picked?"""
    betty_strawberries = 16
    matthew_strawberries = betty_strawberries + 20
    natalie_strawberries = matthew_strawberries / 2
    total_strawberries = betty_strawberries + matthew_strawberries + natalie_strawberries
    jars_of_jam = total_strawberries // 7
    money_made = jars_of_jam * 4
    result = money_made
    return result

print(solution())