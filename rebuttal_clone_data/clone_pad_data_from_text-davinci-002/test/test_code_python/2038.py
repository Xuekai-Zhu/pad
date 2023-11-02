def solution():
    notebooks = 2
    pages_per_notebook = 50
    total_pages = notebooks * pages_per_notebook
    cost = 500
    cost_per_page = cost / total_pages
    result = cost_per_page
    return result

print(solution())