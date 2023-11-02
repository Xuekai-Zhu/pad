def solution():
    """If Giselle has $120, and Isabella has $15 more than Giselle while Sam has $45 less than Isabella,
    calculate the total amount of money each shopper will receive if they donate it to three shoppers
    at their local town's supermarket who then decide to share it equally."""
    
    # Define Giselle's total amount of money
    giselle_money = 120
    
    # Calculate Isabella's and Sam's total amount of money
    isabella_money = giselle_money + 15
    sam_money = isabella_money - 45
    
    # Calculate the total amount of money to be donated
    total_money = giselle_money + isabella_money + sam_money
    
    # Divide the total amount of money equally among 3 shoppers
    each_shopper_money = total_money / 3
    
    # Return the amount of money each shopper will receive
    result = each_shopper_money
    return result

print(solution())