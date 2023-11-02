def solution():
    """Sandra's dog gave birth to 7 puppies. Her vet gave her 105 portions of formula to give to the puppies for 5 days. How many times a day should Sandra feed the puppies?"""
    num_puppies = 7
    num_portions = 105
    num_days = 5
    portions_per_day = num_portions / (num_puppies * num_days)
    result = portions_per_day
    return result

print(solution())