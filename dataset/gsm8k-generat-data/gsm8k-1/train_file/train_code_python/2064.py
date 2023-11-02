def solution():
    """Myrtle’s 3 hens lay 3 eggs a day. She would be gone for 7 days and told her neighbor to take as many as they would like. The neighbor took 12 eggs. Once home, Myrtle collected the remaining eggs, dropping 5 on the way into her house. How many eggs does Myrtle have?"""
    hens = 3
    eggs_per_day = 3
    days_gone = 7
    eggs_taken = 12
    eggs_laid = hens * eggs_per_day * days_gone
    eggs_remaining = eggs_laid - eggs_taken
    eggs_final = eggs_remaining - 5
    result = eggs_final
    return result

print(solution())