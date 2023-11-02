def solution():
    location_of_Nepalese_Civil_War = "Nepal"
    bordering_country = "India"
    if bordering_country in location_of_Nepalese_Civil_War:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())