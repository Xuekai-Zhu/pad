def solution():
    tuition_cost = 22000  # The cost of tuition per semester is $22,000
    parent_contribution = tuition_cost / 2  # Nancy's parents will pay half the tuition
    scholarship_amount = 3000  # Nancy will receive a scholarship for $3,000
    loan_amount = 2 * scholarship_amount  # Nancy will receive a student loan for twice the amount of her scholarship
    total_financial_aid = parent_contribution + scholarship_amount + loan_amount  # Total financial aid available to Nancy
    hours_worked = 200  # Nancy can work a total of 200 hours during the semester
    remaining_tuition = tuition_cost - total_financial_aid  # Nancy needs to pay the remaining tuition

    # Calculate how much Nancy needs to make per hour to pay the remaining tuition
    required_hourly_rate = remaining_tuition / hours_worked
    result = required_hourly_rate
    return result

print(solution())