def solution():
    """Sandra's dog gave birth to 7 puppies. Her vet gave her 105 portions of formula to give to the puppies for 5 days. How many times a day should Sandra feed the puppies?"""
    total_portions = 105
    days = 5
    puppies = 7
    daily_portions = total_portions / (days * puppies)
    result = daily_portions
    return result

print(solution())