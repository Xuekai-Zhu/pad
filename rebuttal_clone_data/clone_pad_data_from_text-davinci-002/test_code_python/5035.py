def solution():
    principal = 300
    rate = 10
    time = 2
    interest = (principal * rate * time) / 100
    total = principal + interest
    result = total
    return result

print(solution())