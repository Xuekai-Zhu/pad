def solution():
    # Define the variables for the problem
    half_spent = 0.5
    spent_after_first_store = 14
    third_spent = 1/3
    spent_after_second_store = 16
    starting_money = 0
    
    # Calculate Mark's total spent at the first store
    total_spent_first_store = half_spent * starting_money + spent_after_first_store
    
    # Calculate Mark's money remaining after the first store
    remaining_money_first_store = starting_money - total_spent_first_store
    
    # Calculate Mark's total spent at the second store
    total_spent_second_store = third_spent * starting_money + spent_after_second_store
    
    # Calculate Mark's money remaining after the second store
    remaining_money_second_store = remaining_money_first_store - total_spent_second_store
    
    # Calculate Mark's starting money
    starting_money = remaining_money_second_store * -1
    
    result = starting_money
    return result

print(solution())