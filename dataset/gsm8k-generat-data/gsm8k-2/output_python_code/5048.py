def solution():
    """Armand is playing a guessing game with his dad where he has to guess a number his dad is thinking of. His dad tells him that the number, when multiplied by 3, is three less than twice 51. What is the number?"""
    equation = (2 * 51) - 3
    number = equation / 3
    result = number
    return result

print(solution())