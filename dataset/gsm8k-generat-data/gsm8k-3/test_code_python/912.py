def solution():
    """Betty picked 16 strawberries. Matthew picked 20 more strawberries than Betty and twice as many as Natalie. They used their strawberries to make jam. One jar of jam used 7 strawberries and they sold each jar at $4. How much money were they able to make from the strawberries they picked?"""
    # Define the number of strawberries each person picked
    betty_strawberries = 16
    natalie_strawberries = betty_strawberries / 2
    matthew_strawberries = betty_strawberries + 20 + (natalie_strawberries * 2)

    # Calculate the total number of strawberries picked
    total_strawberries = betty_strawberries + natalie_strawberries + matthew_strawberries

    # Calculate the number of jars of jam they could make
    jam_jars = total_strawberries // 7

    # Calculate the total revenue from selling the jars of jam
    revenue = jam_jars * 4

    # Display the total revenue
    result = revenue
    return result

print(solution())