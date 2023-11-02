def solution():
    """Kathleen saved $21 in June, $46 in July, and $45 in August. Then Kathleen spent $12 on school supplies and $54 on new clothes. Kathleen’s aunt said she would give Kathleen $25 if Kathleen saves more than $125. How much money does Kathleen have left?"""
    savings = 21 + 46 + 45
    expenses = 12 + 54
    total_money = savings - expenses
    if total_money > 125:
        total_money += 25
    result = total_money
    return result

print(solution())