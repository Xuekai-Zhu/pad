def solution():
    """Troy's home is 75 meters away from school while Emily's home is 98 meters away from school. Troy and Emily walk to school and back home every day. How much farther does Emily walk to school and back in five days?"""
    # Define the distance of Troy's home from school
    troy_distance = 75

    # Define the distance of Emily's home from school
    emily_distance = 98

    # Calculate the total distance Troy walks in one day
    troy_total_distance = troy_distance * 2

    # Calculate the total distance Emily walks in one day
    emily_total_distance = emily_distance * 2

    # Calculate the total distance Emily walks farther in five days compared to Troy
    difference_distance = (emily_total_distance - troy_total_distance) * 5

    # Display the difference in distance walked
    result = difference_distance
    return result

print(solution())