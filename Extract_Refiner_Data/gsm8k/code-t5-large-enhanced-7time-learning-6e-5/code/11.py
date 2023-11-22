def solution():
    
    # Define the prices of the purchase plans
    jewelry_price = 5000
    electronic_gadgets_price = 8000

    # Calculate the profit after the jewelry market rise up
    jewelry_profit = jewelry_price * 0.05

    # Calculate the profit after the electronic gadgets market rise up
    electronic_gadgets_profit = electronic_gadgets_price * 0.02

    # Calculate the total profit after the purchase plans
    total_profit = jewelry_profit + electronic_gadgets_profit

    # Display the total profit
    result = total_profit
    return result

print(solution())