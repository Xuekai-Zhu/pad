def solution():
    # Calculate Celia's total spending for the month
    food_spending = 100 * 4  # $100 a week for 4 weeks
    rent_spending = 1500  # for rent for her apartment
    other_spending = 30 + 50  # for video streaming services and cell phone usage
    total_spending = food_spending + rent_spending + other_spending

    # Calculate the amount to put into savings
    savings = total_spending * 0.1
    result = savings
    return result

print(solution())