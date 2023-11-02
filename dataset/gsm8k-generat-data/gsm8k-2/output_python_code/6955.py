def solution():
    """Viggo spent $80 on a shirt. He paid the shirt using $20 and $10 bills. If she gave the clerk one more $20 bill than $10 bills, how many $10 bills did he give?"""
    shirt_cost = 80
    num_tens = x
    num_twenties = x + 1
    total_twenty_value = num_twenties * 20
    remaining_cost = shirt_cost - total_twenty_value
    num_tens = remaining_cost / 10
    result = num_tens
    return result

print(solution())