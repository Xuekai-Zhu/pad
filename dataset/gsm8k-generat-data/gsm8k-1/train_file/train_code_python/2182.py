def solution():
    """Andrew installed hardwood flooring in his house. His bedroom took eight wooden planks, his living room took twenty planks, and his kitchen took eleven planks. The guest bedroom took two fewer planks than Andrew’s bedroom, and each of his two hallways took four planks. He accidentally ruined three planks in each bedroom by dragging furniture over them and had to replace them. He ended up with six leftover planks at the end. How many wooden planks did Andrew buy to start with?"""
    bedroom_planks = 8 + 3
    living_room_planks = 20
    kitchen_planks = 11
    guest_bedroom_planks = bedroom_planks - 2 + 3
    hallway_planks = 4 * 2
    total_planks = bedroom_planks + living_room_planks + kitchen_planks + guest_bedroom_planks + hallway_planks - 6
    result = total_planks
    return result

print(solution())