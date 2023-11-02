def solution():
    """Clive is buying olives for dinner. He has $10 to spend and needs 80 olives. A jar of 20 olives costs $1.50. How much change will Clive have when he buys what he needs?"""
    budget = 10
    needed_olives = 80
    olives_per_jar = 20
    jar_cost = 1.5
    jars_needed = (needed_olives / olives_per_jar)
    total_cost = jars_needed * jar_cost
    change = budget - total_cost
    result = change
    return result

print(solution())