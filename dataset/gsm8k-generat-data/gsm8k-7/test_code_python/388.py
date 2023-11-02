def solution():
    num_subletters = 3
    subletter_rent = 400
    apartment_rent = 900
    
    # Calculate John's total monthly profits from subletting
    monthly_sublet_profit = (num_subletters * subletter_rent) - apartment_rent
    
    # Calculate John's total yearly profits from subletting
    yearly_sublet_profit = monthly_sublet_profit * 12
    
    result = yearly_sublet_profit
    return result

print(solution())