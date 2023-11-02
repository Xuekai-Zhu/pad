def solution():
    """Betty picked 16 strawberries. Matthew picked 20 more strawberries than Betty and twice as many as Natalie.
    They used their strawberries to make jam. One jar of jam used 7 strawberries and they sold each jar at $4. How much
    money were they able to make from the strawberries they picked?"""
    betty = 16
    matthew = betty + 20
    natalie = betty / 2
    total_strawberries = betty + matthew + natalie
    jars_of_jam = total_strawberries // 7
    price_per_jar = 4
    total_profit = jars_of_jam * price_per_jar
    result = total_profit
    return result

print(solution())