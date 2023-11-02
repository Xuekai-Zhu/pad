def solution():
    first_site = 3700
    second_site = first_site - 352
    third_site = first_site - 3700
    fourth_site = third_site * 2
    fourth_site_date = 8400
    second_site_date = fourth_site_date - fourth_site + second_site
    result = second_site_date
    
    return result

print(solution())