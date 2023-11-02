def solution():
    """James does chores around the class. There are 3 bedrooms, 1 living room, and 2 bathrooms to clean. The bedrooms each take 20 minutes to clean.
    The living room takes as long as the 3 bedrooms combined. The bathroom takes twice as long as the living room. He also cleans the outside which takes twice as long as cleaning the house.
    He splits the chores with his 2 siblings who are just as fast as him. How long, in hours, does he work?"""
    # Define the time it takes to clean each room
    bedroom_time = 20
    living_room_time = 3 * bedroom_time
    bathroom_time = 2 * living_room_time

    # Calculate the total time to clean the inside of the house
    total_inside_time = (3 * bedroom_time) + living_room_time + (2 * bathroom_time)

    # Calculate the time to clean the outside of the house
    outside_time = 2 * total_inside_time

    # Calculate the total time to do all the chores
    total_time = (total_inside_time + outside_time) / 3

    # Convert the total time to hours
    total_hours = total_time / 60

    # Return the result
    result = total_hours
    return result

print(solution())