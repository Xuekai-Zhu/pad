def solution():
    """An archaeologist discovered three dig sites from different periods in one area. The archaeologist dated the first dig site as 352 years more recent than the second dig site. The third dig site was dated 3700 years older than the first dig site. The fourth dig site was twice as old as the third dig site. The archaeologist studied the fourth dig site’s relics and gave the site a date of 8400 BC. What year did the archaeologist date the second dig site?"""
    
    # Calculate the age of the fourth dig site in years
    fourth_dig_age = 8400 + 2000 # 2000 BC is 2000 years before 0 AD

    # Calculate the age of the third dig site in years
    third_dig_age = fourth_dig_age / 2

    # Calculate the age of the first dig site in years
    first_dig_age = third_dig_age - 3700

    # Calculate the age of the second dig site in years
    second_dig_age = first_dig_age - 352

    # Convert the age of the second dig site from years to BC
    second_dig_year = abs(second_dig_age - 1)

    # Display the year the archaeologist dated the second dig site
    result = second_dig_year
    return result

print(solution())