def solution():
    """Jenny is older than Charlie by five years, while Charlie is older than Bobby by three years. How old will Charlie be when Jenny becomes twice as old as Bobby?"""
    # Let's assume Bobby's current age to be x
    x = 1
    # Charlie is older than Bobby by 3 years, so his current age will be x+3
    charlie_age = x + 3
    # Jenny is older than Charlie by 5 years, so her current age will be x+8
    jenny_age = x + 8
    # We need to find out at what age Charlie will be when Jenny becomes twice as old as Bobby
    # Let's assume y be the number of years after which this will happen
    y = (jenny_age - 2*x)/2 
    # Charlie's age when this happens will be y + charlie_age
    result = y + charlie_age
    return result

print(solution())