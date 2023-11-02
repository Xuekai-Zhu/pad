def solution():
    """The sum of Cooper's, Dante's, and Maria's ages is 31. Dante is twice as old as Cooper. Maria is one year older than Dante. How old is Cooper?"""
    total_age = 31
    dante_age = 2 * cooper_age
    maria_age = dante_age + 1
    cooper_age = (total_age - dante_age - maria_age) / 3
    result = int(cooper_age)
    return result

print(solution())