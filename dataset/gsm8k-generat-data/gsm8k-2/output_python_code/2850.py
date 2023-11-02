def solution():
    """Aaron, Henry's brother, is 15 years old. Henry's sister is three times as old as Aaron. Henry is four times as old as his sister. What's the combined age of the siblings?"""
    aaron_age = 15
    henry_sister_age = 3 * aaron_age
    henry_age = 4 * henry_sister_age
    total_age = aaron_age + henry_sister_age + henry_age
    result = total_age
    return result

print(solution())