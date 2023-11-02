def solution():
    """Matt wants to repaint his house. He needs to paint three walls in his living room, which is a square 40 feet by 40 feet, and all four walls in his bedroom, which is a rectangle 10 feet by 12 feet. All the walls in Matt's house are 10 feet tall. How many total square feet of wall does Matt need to paint?"""
    # Define the dimensions of the living room
    living_room_length = 40
    living_room_width = 40
    living_room_height = 10

    # Define the dimensions of the bedroom
    bedroom_length = 12
    bedroom_width = 10
    bedroom_height = 10

    # Calculate the area of the living room walls
    living_room_area = 2 * living_room_height * (living_room_length + living_room_width)
    # There are three walls to paint, so we multiply the area by 3
    living_room_wall_area = 3 * living_room_area

    # Calculate the area of the bedroom walls
    bedroom_area = 2 * bedroom_height * (bedroom_length + bedroom_width)
    # There are four walls to paint, so we multiply the area by 4
    bedroom_wall_area = 4 * bedroom_area

    # Calculate the total area of all the walls to paint
    total_wall_area = living_room_wall_area + bedroom_wall_area

    # Display the total wall area to paint
    result = total_wall_area
    return result

print(solution())