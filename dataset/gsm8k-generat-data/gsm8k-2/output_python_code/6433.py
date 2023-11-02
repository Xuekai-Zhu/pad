def solution():
    """Clive is buying olives for dinner. He has $10 to spend and needs 80 olives. A jar of 20 olives costs $1.50. How much change will Clive have when he buys what he needs?"""
    num_olives_needed = 80
    jar_size = 20
    jar_price = 1.5
    num_jars_needed = (num_olives_needed // jar_size) + (num_olives_needed % jar_size > 0)
    total_price = num_jars_needed * jar_price
    change = 10 - total_price
    result = change
    return result

print(solution())