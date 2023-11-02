def solution():
    
    quarter_piles = 4
    dime_piles = 6
    nickel_piles = 9
    penny_piles = 5

    
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    penny_value = 1

    total_quarters = quarter_piles * 10  
    total_dimes = dime_piles * 10
    total_nickels = nickel_piles * 10
    total_pennies = penny_piles * 10

    
    total_value = (total_quarters * quarter_value) + (total_dimes * dime_value) + (total_nickels * nickel_value) + (
                total_pennies * penny_value)

    
    total_value /= 100.0

    result = total_value
    return result

print(solution())