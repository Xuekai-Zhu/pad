def solution():
    adam_magnets = 18
    peter_magnets = adam_magnets * 2  # Peter has twice as many magnets as Adam after giving away a third
    adam_magnets -= adam_magnets / 3  # Adam gave away a third of his magnets

    # Check if Adam's remaining magnets is half of Peter's magnets
    while adam_magnets != peter_magnets / 2:
        peter_magnets += 1
    result = peter_magnets
    return result

print(solution())