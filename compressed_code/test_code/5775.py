def solution():
    
    total_workers = 90
    men = 2/3 * total_workers
    women = total_workers - men
    new_women = 10
    total_women = women + new_women
    total_workers += new_women
    women_percentage = (total_women / total_workers) * 100
    result = women_percentage
    return result

print(solution())