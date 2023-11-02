def solution():
    savings = [21, 46, 45]
    expenses = [12, 54]
    aunt_savings_threshold = 125
    aunt_savings_bonus = 25

    # Calculate the total savings over the three months
    total_savings = sum(savings)

    # Calculate the total expenses
    total_expenses = sum(expenses)

    # Calculate the net savings
    net_savings = total_savings - total_expenses

    # Check if Kathleen saved more than $125
    if net_savings > aunt_savings_threshold:
        net_savings += aunt_savings_bonus

    result = net_savings
    return result

print(solution())