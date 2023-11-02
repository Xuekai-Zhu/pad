def solution():
    """Viggo spent $80 on a shirt. He paid the shirt using $20 and $10 bills. If she gave the clerk one more $20 bill than $10 bills, how many $10 bills did he give?"""
    total_cost = 80
    num_20s = 0
    num_10s = 0
    while total_cost >= 20:
        if num_20s == num_10s + 1:
            num_20s += 1
            total_cost -= 20
        else:
            num_10s += 1
            total_cost -= 10
    result = num_10s
    return result

print(solution())