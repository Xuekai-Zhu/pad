def solution():
    # Calculate the total amount of money Madeline needs to spend this month
    total_expenses = 1200 + 400 + 200 + 60 + 200  # rent + groceries + medical expenses + utilities + emergency savings
    
    # Calculate the number of hours Madeline needs to work to cover her expenses
    hours_needed = total_expenses / 15  # Madeline makes $15 per hour at her job
    
    result = hours_needed
    return result

print(solution())