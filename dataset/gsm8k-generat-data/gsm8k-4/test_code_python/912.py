def solution():
    """Betty picked 16 strawberries. Matthew picked 20 more strawberries than Betty and twice as many as Natalie. They used their strawberries to make jam. One jar of jam used 7 strawberries and they sold each jar at $4. How much money were they able to make from the strawberries they picked?"""
    # Define the number of strawberries picked by Betty
    betty_strawberries = 16

    # Define the number of strawberries picked by Matthew
    matthew_strawberries = betty_strawberries + 20

    # Define the number of strawberries picked by Natalie
    natalie_strawberries = matthew_strawberries / 2

    # Calculate the total number of strawberries picked
    total_strawberries = betty_strawberries + matthew_strawberries + natalie_strawberries

    # Calculate the number of jars of jam they can make
    jars_of_jam = total_strawberries // 7

    # Calculate the total sales from selling the jars of jam
    total_sales = jars_of_jam * 4

    result = total_sales
    return result

print(solution())