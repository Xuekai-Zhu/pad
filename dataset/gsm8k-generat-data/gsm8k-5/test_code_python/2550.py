def solution():
    pay_per_hour = 28 / 4  # Nancy earns $28 for working 4 hours, so she earns $7 per hour
    required_pay = 70  # Nancy wants to earn $70
    hours_needed = required_pay / pay_per_hour  # The number of hours Nancy needs to work to earn $70

    result = hours_needed
    return result

print(solution())