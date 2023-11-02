def solution():
    
    
    library_percent = 15
    library_spending = 3000
    park_percent = 24
    total_spending = library_spending / (library_percent / 100)
    park_spending = total_spending * (park_percent / 100)
    remaining_budget = total_spending - (library_spending + park_spending)
    result = remaining_budget
    
    return result

print(solution())