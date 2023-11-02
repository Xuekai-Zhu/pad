def solution():
    # Define the exchange rates
    dimes_per_quarter = 3
    nickels_per_quarter = 7

    # Calculate the total amount of money traded for each set of 20 quarters
    dimes_traded = 20 * dimes_per_quarter * 0.1
    nickels_traded = 20 * nickels_per_quarter * 0.05

    # Calculate the total amount of money lost by Mac
    total_lost = dimes_traded + nickels_traded - 10 * 20
    result = total_lost
    return result

print(solution())