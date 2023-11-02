def solution():
    # Calculate Vince's earnings
    earnings = 18 * 80  # Vince earns $18 per head and serves 80 customers a month

    # Calculate Vince's expenses and recreation allocation
    expenses = 280  # Vince's monthly expenses for rent and electricity
    recreation = 0.2 * earnings  # 20% of Vince's earnings are allocated for recreation and relaxation

    # Calculate Vince's savings
    savings = earnings - expenses - recreation
    result = savings
    return result

print(solution())