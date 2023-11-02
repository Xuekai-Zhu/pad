def solution():
    """Andrew installed hardwood flooring in his house. His bedroom took eight wooden planks, his living room took twenty planks, and his kitchen took eleven planks. The guest bedroom took two fewer planks than Andrew’s bedroom, and each of his two hallways took four planks. He accidentally ruined three planks in each bedroom by dragging furniture over them and had to replace them. He ended up with six leftover planks at the end. How many wooden planks did Andrew buy to start with?"""
    # Define the number of planks used in each room
    bedroom_planks = 8
    livingroom_planks = 20
    kitchen_planks = 11
    guestbedroom_planks = bedroom_planks - 2
    hallway_planks = 4

    # Calculate the total number of planks used
    total_planks = (bedroom_planks + livingroom_planks + kitchen_planks + guestbedroom_planks + 2*hallway_planks)

    # Calculate the number of planks replaced in the bedrooms
    replaced_planks = 2 * 3

    # Adjust for the replaced planks and the leftover planks
    total_planks = total_planks + replaced_planks + 6

    result = total_planks
    return result

print(solution())