def solution():
    """Aaron, Henry's brother, is 15 years old. Henry's sister is three times as old as Aaron. Henry is four times as old as his sister. What's the combined age of the siblings?"""
    aaron_age = 15
    sister_age = 3 * aaron_age
    henry_age = 4 * sister_age
    combined_age = aaron_age + sister_age + henry_age
    result = combined_age
    return result

print(solution())