def solution():
    """Nancy wants to figure out if she can afford to apply to the University of Michigan. The tuition costs $22,000 per semester. Her parents can pay half the cost, and each semester Nancy can get a scholarship for $3,000 and a student loan for twice her scholarship amount. If Nancy can work a total of 200 hours during the semester, how many dollars does she have to make per hour to pay the rest of the tuition?"""
    # Define the tuition cost
    TUITION_COST = 22000

    # Calculate Nancy's available resources
    parents_payment = 0.5 * TUITION_COST
    scholarship = 3000
    loan = 2 * scholarship
    total_resources = parents_payment + scholarship + loan

    # Calculate how much Nancy needs to earn through work
    remaining_cost = TUITION_COST - total_resources

    # Calculate Nancy's required hourly rate
    hourly_rate = remaining_cost / 200

    # Display Nancy's required hourly rate
    result = hourly_rate
    return result

print(solution())