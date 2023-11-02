def solution():
    
    # Define Valerie's monthly earnings
    valerie_earnings = 5000

    # Calculate the brother's monthly earnings
    brother_earnings = valerie_earnings / 2

    # Calculate the combined salary of Valerie and her brother
    combined_salary = valerie_earnings + brother_earnings

    # Calculate the mother's monthly earnings
    mother_earnings = combined_salary * 2

    # Calculate the total amount of money they all have together
    total_money = valerie_earnings + brother_earnings + mother_earnings

    # Display the total amount of money
    result = total_money
    return result

print(solution())