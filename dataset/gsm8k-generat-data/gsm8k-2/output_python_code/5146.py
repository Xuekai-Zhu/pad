def solution():
    """Rachel makes $12.00 as a waitress in a coffee shop. In one hour, she serves 20 different people and they all leave her a $1.25 tip. How much money did she make in that hour?"""
    base_pay = 12.00
    num_customers = 20
    tip_amount = 1.25
    total_tips = num_customers * tip_amount
    total_earnings = base_pay + total_tips
    result = total_earnings
    return result

print(solution())