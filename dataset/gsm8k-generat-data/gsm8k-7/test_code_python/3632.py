def solution():
    num_notebooks = 2
    pages_per_notebook = 50
    total_pages = num_notebooks * pages_per_notebook
    total_cost = 500  # in cents, since $5 = 500 cents
    cost_per_page = total_cost / total_pages
    result = cost_per_page
    return result

print(solution())