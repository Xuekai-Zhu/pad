def solution():
    
    john_age = 10
    sister_age = john_age * 2
    age_difference = sister_age - john_age
    future_age = 50
    future_sister_age = sister_age + (future_age - john_age)
    result = future_sister_age
    return result

print(solution())