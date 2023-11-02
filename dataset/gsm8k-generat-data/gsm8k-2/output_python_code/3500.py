def solution():
    """Chenny bought 9 plates at $2 each. She also bought spoons at $1.50 each. How many spoons did Chenny buy if she paid a total of $24 for the plates and spoon?"""
    plates_price = 2
    plates_count = 9
    plates_total = plates_price * plates_count
    total_price = 24
    spoons_price = 1.5
    spoons_total = total_price - plates_total
    spoons_count = spoons_total / spoons_price
    result = spoons_count
    return result

print(solution())