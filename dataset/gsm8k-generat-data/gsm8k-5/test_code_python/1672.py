def solution():
    current_age_lennon = 8
    years_to_add = 2
    ratio_of_ages = 4  # Ophelia will be four times as old as Lennon in two years

    # Calculate Lennon's age in two years, then use it to find Ophelia's age in two years
    age_lennon_in_two_years = current_age_lennon + years_to_add
    age_ophelia_in_two_years = age_lennon_in_two_years * ratio_of_ages

    # Use Ophelia's age in two years to find her current age
    current_age_ophelia = age_ophelia_in_two_years - years_to_add
    result = current_age_ophelia
    return result

print(solution())