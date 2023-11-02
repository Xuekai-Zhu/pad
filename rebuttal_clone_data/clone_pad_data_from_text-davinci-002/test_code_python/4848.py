def solution():
    women_employees = 0.6
    men_employees = 0.4
    college_educated_men = 0.75
    non_college_educated_men = 0.25
    total_employees = 1
    
    women_employees = total_employees * women_employees
    men_employees = total_employees * men_employees
    
    total_college_educated_men = college_educated_men * men_employees
    total_non_college_educated_men = non_college_educated_men * men_employees
    
    total_college_educated = total_college_educated_men + women_employees
    total_non_college_educated = total_non_college_educated_men
    
    result = total_college_educated, total_non_college_educated
    
    return result

print(solution())