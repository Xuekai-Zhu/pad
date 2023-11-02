def solution():
    
    total_scientists = 70
    europe_scientists = total_scientists / 2
    canada_scientists = total_scientists / 5
    usa_scientists = total_scientists - europe_scientists - canada_scientists
    result = usa_scientists
    return result

print(solution())