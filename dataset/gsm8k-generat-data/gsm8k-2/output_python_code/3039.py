def solution():
    """Tim is 5 years old. His cousin, Rommel, is thrice as old as he is. His other cousin, Jenny, is 2 years older than Rommel. How many years younger is Tim than Jenny?"""
    tim_age = 5
    rommel_age = tim_age * 3
    jenny_age = rommel_age + 2
    difference = jenny_age - tim_age
    result = difference
    return result

print(solution())