def solution():
    """Alice is 7 years older than Beth, who is 5 years older than Erica. What is the difference between the ages of Alice and Erica, if Erica is 30 years old?"""
    erica_age = 30
    beth_age = erica_age - 5
    alice_age = beth_age + 7
    diff = alice_age - erica_age
    result = diff
    return result

print(solution())