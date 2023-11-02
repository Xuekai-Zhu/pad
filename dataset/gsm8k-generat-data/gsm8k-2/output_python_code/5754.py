def solution():
    """John is twice as old as Mary and half as old as Tonya. If Tanya is 60, what is their average age?"""
    tanya_age = 60
    john_age = tanya_age / 2
    mary_age = john_age / 2
    tonya_age = tanya_age * 2
    avg_age = (john_age + mary_age + tonya_age) / 3
    result = avg_age
    return result

print(solution())