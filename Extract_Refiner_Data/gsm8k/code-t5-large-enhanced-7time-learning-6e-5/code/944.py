def solution():
    
    # Define the commission rates
    NY_COMMISSION_RATE = 0.1
    WALLET_COMMISSION_RATE = 0.08

    # Define the number of copies of each type sold
    NY_COPIES = 6
    WALLET_COPIES = 10

    # Calculate the commission earned on each type of copy
    NY_COMMISSION = NY_COMMISSION_RATE * NY_COPIES
    WALLET_COMMISSION = WALLET_COMMISSION_RATE * WALLET_COPIES

    # Calculate the total commission earned
    total_commission = NY_COMMISSION + WALLET_COMMISSION

    # Display the total commission earned
    result = total_commission
    return result

print(solution())