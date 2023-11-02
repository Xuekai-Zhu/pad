def solution():
    # Calculate the new value of Josh's stocks after the 30% increase
    new_stock_value = 2000 * 1.3

    # Calculate the total value of Josh's assets
    total_value = new_stock_value + 300

    # Calculate the amount of money Josh will have in his wallet after selling all of his stocks
    wallet_money = total_value - new_stock_value

    result = wallet_money
    return result

print(solution())