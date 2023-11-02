def solution():
    
    husband_weekly_savings = 335
    wife_weekly_savings = 225
    total_weekly_savings = husband_weekly_savings + wife_weekly_savings
    weekly_savings_in_6_months = total_weekly_savings * 4 * 6
    total_savings_in_6_months = weekly_savings_in_6_months
    half_of_total_savings = total_savings_in_6_months / 2
    each_child_receives = half_of_total_savings / 4
    result = each_child_receives
    return result

print(solution())