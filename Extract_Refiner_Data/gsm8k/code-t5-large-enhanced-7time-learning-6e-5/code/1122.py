def solution():
    
    # Define the distance that Alfie flies every day
    daily_distance = 400

    # Define the circumference of the earth
    earth_distance = 40000

    # Calculate the distance that Alfie needs to fly to cover half of the earth
    half_distance = earth_distance / 2

    # Calculate the number of days it will take Alfie to fly a distance equal to half of the way around the earth
    days_to_fly = half_distance / daily_distance / daily_distance

    # Display the number of days
    result = days_to_fly
    return result

print(solution())