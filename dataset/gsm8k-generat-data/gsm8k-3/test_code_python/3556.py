def solution():
    """Kathleen saved $21 in June, $46 in July, and $45 in August. Then Kathleen spent $12 on school supplies and $54 on new clothes. Kathleen's aunt said she would give Kathleen $25 if Kathleen saves more than $125. How much money does Kathleen have left?"""
    # Calculate Kathleen's total savings
    total_savings = 21 + 46 + 45

    # Calculate Kathleen's total expenses
    total_expenses = 12 + 54

    # Calculate Kathleen's total remaining money
    remaining_money = total_savings - total_expenses

    # Check if Kathleen saved more than $125
    if total_savings > 125:
        remaining_money += 25

    # Display the remaining money
    result = remaining_money
    return result

print(solution())