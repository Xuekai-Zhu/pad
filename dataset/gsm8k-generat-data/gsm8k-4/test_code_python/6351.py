def solution():
    """Telegraph Road goes through multiple states and is 162 kilometers long. Pardee Road is 12000 meters long. How many kilometers longer is Telegraph Road than Pardee Road?"""
    # Define the length of Telegraph Road and Pardee Road in meters
    telegraph_meters = 162000
    pardee_meters = 12000

    # Convert the length of Pardee Road to meters
    pardee_kilometers = pardee_meters / 1000

    # Convert the length of Telegraph Road to kilometers
    telegraph_kilometers = telegraph_meters / 1000

    # Calculate the difference in length between Telegraph Road and Pardee Road
    difference = telegraph_kilometers - pardee_kilometers

    # Round the result to 2 decimal places
    result = round(difference, 2)
    return result

print(solution())