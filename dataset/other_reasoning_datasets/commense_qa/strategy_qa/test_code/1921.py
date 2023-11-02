def solution():
    stomach_irritants = ["alcohol", "coffee", "acidic foods"]
    lemon_acidity = "high"
    if lemon_acidity in stomach_irritants:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())