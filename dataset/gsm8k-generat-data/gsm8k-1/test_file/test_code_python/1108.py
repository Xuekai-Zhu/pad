def solution():
    """Pierre, Paul, and Jacques bought 12 kg of apples. Peter wants a quarter of that and Paul wants 1/3 of that. How many kilograms will James have left?"""
    total_apples = 12
    peter_apples = total_apples / 4
    paul_apples = total_apples / 3
    james_apples = total_apples - peter_apples - paul_apples
    result = james_apples
    return result

print(solution())