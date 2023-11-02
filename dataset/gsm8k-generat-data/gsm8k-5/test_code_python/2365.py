def solution():
    fourth_site_years_ago = 8400  # The fourth dig site was dated 8400 years ago
    third_site_years_ago = fourth_site_years_ago / 2  # The third site was twice as old as the fourth site
    first_site_years_ago = third_site_years_ago - 3700  # The first site was 3700 years older than the third site
    second_site_years_ago = first_site_years_ago - 352  # The second site was 352 years more recent than the first site

    # Calculate the year the archaeologist dated the second dig site
    current_year = 2021  # This is the current year
    second_site_year = current_year - second_site_years_ago
    result = second_site_year
    return result

print(solution())