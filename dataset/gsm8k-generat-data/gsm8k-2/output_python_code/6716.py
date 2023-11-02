def solution():
    """In four years, Peter will be twice as old as Harriet. If Peter's age is currently half of his mother's age, who is 60, how old is Harriet now?"""
    mother_age = 60
    peter_age = mother_age / 2
    harriet_age = (peter_age * 2) - 4
    result = harriet_age
    return result

print(solution())