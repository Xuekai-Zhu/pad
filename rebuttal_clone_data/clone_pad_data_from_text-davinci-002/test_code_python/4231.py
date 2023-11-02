def solution():
    people = 25
    gallons_per_person = 0.5
    gallons_per_day = people * gallons_per_person
    miles_per_day = 200
    total_miles = 4000
    travel_days = total_miles / miles_per_day
    total_gallons = gallons_per_day * travel_days
    result = total_gallons
    return result

print(solution())