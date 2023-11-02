def solution():
    """At Palm Meadows, there are 13 hotel rooms. Eight of the rooms have two beds in them and the rest have three beds. How many beds are there in total?"""
    # Define the number of rooms with two beds and the number of rooms with three beds
    rooms_with_two_beds = 8
    rooms_with_three_beds = 13 - rooms_with_two_beds

    # Calculate the total number of beds
    total_beds = (rooms_with_two_beds * 2) + (rooms_with_three_beds * 3)

    # Display the total number of beds
    result = total_beds
    return result

print(solution())