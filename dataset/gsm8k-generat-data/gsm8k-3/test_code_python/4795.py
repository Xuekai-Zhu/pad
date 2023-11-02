def solution():
    """James does chores around the class.  There are 3 bedrooms, 1 living room, and 2 bathrooms to clean.  The bedrooms each take 20 minutes to clean.  The living room takes as long as the 3 bedrooms combined.  The bathroom takes twice as long as the living room.  He also cleans the outside which takes twice as long as cleaning the house.  He splits the chores with his 2 siblings who are just as fast as him.  How long, in hours, does he work?"""
    # Define the time it takes to clean the bedrooms
    bedroom_time = 20 * 3

    # Define the time it takes to clean the living room
    living_room_time = bedroom_time * 3

    # Define the time it takes to clean the bathrooms
    bathroom_time = living_room_time * 2

    # Define the time it takes to clean the house
    house_time = bedroom_time + living_room_time + bathroom_time

    # Define the time it takes to clean the outside
    outside_time = house_time * 2

    # Define the total time it takes for James and his siblings to clean the house
    total_time = (house_time + outside_time) / 3

    # Convert the total time to hours
    total_time_hours = total_time / 60

    # Display the total time in hours
    result = total_time_hours
    return result

print(solution())