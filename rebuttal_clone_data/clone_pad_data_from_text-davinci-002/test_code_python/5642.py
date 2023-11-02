def solution():
    Christine_strawberries = 10
    Rachel_strawberries = Christine_strawberries * 2
    strawberries_needed_per_pie = 3
    Christine_pies = Christine_strawberries / strawberries_needed_per_pie
    Rachel_pies = Rachel_strawberries / strawberries_needed_per_pie
    total_pies = Christine_pies + Rachel_pies
    result = total_pies
    return result

print(solution())