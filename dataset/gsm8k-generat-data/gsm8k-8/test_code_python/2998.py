def solution():
    katherine_time_per_website = 20
    naomi_time_per_website = 1.25 * katherine_time_per_website # Naomi takes 1/4 more time than Katherine
    naomi_websites = 30

    total_time_naomi = naomi_time_per_website * naomi_websites
    result = total_time_naomi
    return result

print(solution())