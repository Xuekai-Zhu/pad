def solution():
    singer_pay = 15 * 3  # pay for 3 hours at $15 per hour
    tip = 0.2 * singer_pay  # 20% tip on the singer's pay
    total_pay = singer_pay + tip  # total amount paid including tip
    result = total_pay
    return result

print(solution())