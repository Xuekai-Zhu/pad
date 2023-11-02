def solution():
    """An archaeologist discovered three dig sites from different periods in one area. The archaeologist dated the first dig site as 352 years more recent than the second dig site. The third dig site was dated 3700 years older than the first dig site. The fourth dig site was twice as old as the third dig site. The archaeologist studied the fourth dig site’s relics and gave the site a date of 8400 BC. What year did the archaeologist date the second dig site?"""
    
    fourth_dig_site_age = 8400
    third_dig_site_age = fourth_dig_site_age / 2
    first_dig_site_age = third_dig_site_age - 3700
    second_dig_site_age = first_dig_site_age - 352
    
    # Convert years BC to AD
    second_dig_site_date = -second_dig_site_age + 1
    
    result = second_dig_site_date
    return result

print(solution())