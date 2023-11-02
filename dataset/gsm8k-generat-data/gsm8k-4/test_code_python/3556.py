def solution():
    """Kathleen saved $21 in June, $46 in July, and $45 in August. Then Kathleen spent $12 on school supplies and $54 on new clothes. Kathleen’s aunt said she would give Kathleen $25 if Kathleen saves more than $125. How much money does Kathleen have left?"""
    # Define the savings and expenses
    savings = 21 + 46 + 45
    expenses = 12 + 54

    # Calculate the total money left
    total_money = savings - expenses

    # Check if the total money is greater than $125
    if total_money > 125:
        aunt_gift = 25
        total_money += aunt_gift

    result = total_money
    return result

print(solution())