def solution():
    current_year = 2021 #update current year if needed
    popular_threshold = 10 #years of popularity considered significant
    original_release_year = 1982
    most_recent_edition_year = 2007
    years_since_original_release = current_year - original_release_year
    years_since_most_recent_edition = current_year - most_recent_edition_year
    if years_since_original_release >= popular_threshold and years_since_most_recent_edition <= popular_threshold:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())