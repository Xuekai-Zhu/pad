def solution():
    """Toby’s father gave him $343 for passing the test. Toby decided to share it with his two brothers, so he gave each of them 1/7 of $343. How many dollars are left for Toby?"""
    # Define the total amount of money Toby's father gave him
    total_money = 343
    
    # Calculate the amount of money each brother received
    money_per_brother = total_money * (1/7)
    
    # Calculate the total amount of money Toby gave to his brothers
    total_money_given = money_per_brother * 2
    
    # Calculate how much money Toby has left
    money_left = total_money - total_money_given
    
    # Display how much money Toby has left
    result = money_left
    return result

print(solution())