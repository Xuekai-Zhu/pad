def solution():
    """An archaeologist discovered three dig sites from different periods in one area. The archaeologist dated the first dig site as 352 years more recent than the second dig site. The third dig site was dated 3700 years older than the first dig site. The fourth dig site was twice as old as the third dig site. The archaeologist studied the fourth dig site’s relics and gave the site a date of 8400 BC. What year did the archaeologist date the second dig site?"""
    fourth_site_date = -8400  # BC is considered negative in this context
    third_site_date = fourth_site_date / 2
    first_site_date = third_site_date - 3700
    second_site_date = first_site_date - 352
    result = second_site_date
    return result

print(solution())