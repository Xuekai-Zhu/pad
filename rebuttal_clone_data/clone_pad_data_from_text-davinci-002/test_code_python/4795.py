def solution():
    bedrooms = 3
    minutes_per_bedroom = 20
    total_minutes_ cleaning_bedrooms = bedrooms * minutes_per_bedroom
    living_room = 1
    minutes_per_living_room = total_minutes_cleaning_bedrooms
    total_minutes_cleaning_living_room = living_room * minutes_per_living_room
    bathroom = 2
    minutes_per_bathroom = minutes_per_living_room * 2
    total_minutes_cleaning_bathrooms = bathroom * minutes_per_bathroom
    outside = 2
    minutes_per_outside = minutes_per_living_room * 2
    total_minutes_cleaning_outside = outside * minutes_per_outside
    siblings = 2
    total_hours = (total_minutes_cleaning_bedrooms + total_minutes_cleaning_living_room + total_minutes_cleaning_bathrooms + total_minutes_cleaning_outside) / (60 * siblings)
    result = total_hours
    return result

print(solution())