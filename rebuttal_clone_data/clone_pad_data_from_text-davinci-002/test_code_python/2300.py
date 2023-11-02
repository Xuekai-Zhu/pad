def solution():
    hours_worked_by_josh = 8
    hours_worked_by_carl = hours_worked_by_josh - 2
    days_worked_by_josh = 5
    days_worked_by_carl = days_worked_by_josh
    weeks_worked = 4
    hours_worked_by_josh_in_a_month = hours_worked_by_josh * days_worked_by_josh * weeks_worked
    hours_worked_by_carl_in_a_month = hours_worked_by_carl * days_worked_by_carl * weeks_worked
    wage_of_josh = 9
    wage_of_carl = wage_of_josh / 2
    total_wages = (hours_worked_by_josh_in_a_month * wage_of_josh) + (hours_worked_by_carl_in_a_month * wage_of_carl)
    result = total_wages
    
    return result

print(solution())