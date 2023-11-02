def solution():
    """Andrew installed hardwood flooring in his house. His bedroom took eight wooden planks, his living room took twenty planks, and his kitchen took eleven planks. The guest bedroom took two fewer planks than Andrew’s bedroom, and each of his two hallways took four planks. He accidentally ruined three planks in each bedroom by dragging furniture over them and had to replace them. He ended up with six leftover planks at the end. How many wooden planks did Andrew buy to start with?"""
    # Calculate the number of planks in Andrew's main rooms
    bedroom_planks = 8
    living_room_planks = 20
    kitchen_planks = 11
    guest_bedroom_planks = bedroom_planks - 2
    hallway_planks = 4 * 2

    # Calculate the total number of planks before replacement
    total_planks = (
        bedroom_planks
        + living_room_planks
        + kitchen_planks
        + guest_bedroom_planks
        + hallway_planks
    )

    # Calculate the total number of planks after replacement
    total_planks -= 3 * 2

    # Add six leftover planks
    total_planks += 6

    # Display the total number of planks
    result = total_planks
    return result

print(solution())