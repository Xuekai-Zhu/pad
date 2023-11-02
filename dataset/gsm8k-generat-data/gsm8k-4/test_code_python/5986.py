def solution():
    """Nancy wants to figure out if she can afford to apply to the University of Michigan. The tuition costs $22,000 per semester. Her parents can pay half the cost, and each semester Nancy can get a scholarship for $3,000 and a student loan for twice her scholarship amount. If Nancy can work a total of 200 hours during the semester, how many dollars does she have to make per hour to pay the rest of the tuition?"""
    
    # Define the tuition cost, the scholarship amount, and the number of hours Nancy can work
    tuition = 22000
    scholarship = 3000
    hours_worked = 200
    
    # Calculate the amount Nancy's parents will pay
    parents_payment = tuition / 2
    
    # Calculate the total amount of financial aid Nancy can receive
    total_aid = scholarship + (2 * scholarship)
    
    # Calculate the total amount Nancy needs to pay
    total_payment = tuition - parents_payment - total_aid
    
    # Calculate the hourly wage Nancy needs to earn to pay the rest of the tuition
    hourly_wage = total_payment / hours_worked
    
    result = hourly_wage
    return result

print(solution())