def solution():
    """John needs to take 2 pills a day. One pill costs $1.5. The insurance covers 40% of the cost. How much does he pay in a 30-day month?"""
    pills_per_day = 2
    cost_per_pill = 1.5
    days_per_month = 30
    insurance_coverage = 0.4

    # Calculate the total cost of pills without insurance coverage
    total_cost_no_coverage = pills_per_day * cost_per_pill * days_per_month

    # Calculate the total cost of pills with insurance coverage
    total_cost_with_coverage = total_cost_no_coverage * (1 - insurance_coverage)

    # Calculate the amount John pays out of pocket
    out_of_pocket = total_cost_with_coverage * insurance_coverage

    # Display the amount John pays out of pocket
    result = out_of_pocket
    return result

print(solution())