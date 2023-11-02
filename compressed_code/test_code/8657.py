def solution():
    
    num_notebooks = 2
    pages_per_notebook = 50
    total_pages = num_notebooks * pages_per_notebook
    total_cost_cents = 500  
    cost_per_page_cents = total_cost_cents / total_pages
    result = cost_per_page_cents
    return result

print(solution())