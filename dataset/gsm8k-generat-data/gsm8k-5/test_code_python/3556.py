def solution():
    savings = 21 + 46 + 45  # Kathleen saved $21 in June, $46 in July, and $45 in August
    expenses = 12 + 54  # Kathleen spent $12 on school supplies and $54 on new clothes
    total_money = savings - expenses  # Total money Kathleen has
    if total_money > 125:
        total_money += 25  # Kathleen's aunt gave her $25 as she saved more than $125
    result = total_money
    return result

print(solution())