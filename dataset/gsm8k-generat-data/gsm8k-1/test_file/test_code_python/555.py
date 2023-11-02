def solution():
    """A stickler for health, Octavia drinks half the daily recommended cups of coffee. By contract, Octavia’s husband Juan drinks 10 times the amount of coffee she drinks. Juan’s doctor has asked him to reduce his coffee intake to the daily recommendation of 4 cups. By how many cups must Juan reduce his daily coffee intake?"""
    octavia_cups = 1/2
    juan_cups = octavia_cups * 10
    reduce_by = juan_cups - 4
    result = reduce_by
    return result

print(solution())