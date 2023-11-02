def solution():
    total_people = 84  # There are 84 people waiting in line
    cars_per_ride = 7  # The roller coaster has 7 cars
    seats_per_car = 2  # Each car seats 2 people

    # Calculate the number of people that can ride in one trip
    people_per_ride = cars_per_ride * seats_per_car

    # Calculate the number of trips needed to give everyone a turn
    trips_needed = total_people // people_per_ride

    # If there are leftover people, add one more trip
    if total_people % people_per_ride != 0:
        trips_needed += 1

    result = trips_needed
    return result

print(solution())