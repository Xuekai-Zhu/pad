def solution():
    # Define the variables
    tuition_cost = 22000
    parents_payment = tuition_cost / 2
    scholarship_amount = 3000
    loan_amount = 2 * scholarship_amount
    total_hours = 200

    # Calculate the total amount of money Nancy can use towards tuition each semester
    total_money = parents_payment + scholarship_amount + loan_amount
    
    # Calculate how much money Nancy needs to earn per hour to cover the remaining tuition cost
    remaining_cost = tuition_cost - total_money
    hourly_rate = remaining_cost / total_hours
    result = hourly_rate
    return result

print(solution())