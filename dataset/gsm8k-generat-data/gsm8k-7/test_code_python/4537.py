def solution():
    savings = 0
    for i in range(3):
        savings += int(input(f"How much did Miranda save in month {i+1}?\n"))
    total_cost = 260
    sister_gift = 50
    total_savings = savings + sister_gift
    monthly_savings = total_savings / 3
    result = monthly_savings
    return result

print(solution())