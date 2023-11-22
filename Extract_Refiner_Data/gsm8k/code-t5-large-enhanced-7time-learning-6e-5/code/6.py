def solution():
    
    first_month_downloads = 60
    second_month_downloads = first_month_downloads * 3
    third_month_downloads = second_month_downloads * 0.7
    total_downloads = first_month_downloads + second_month_downloads + third_month_downloads
    result = total_downloads
    return result

print(solution())