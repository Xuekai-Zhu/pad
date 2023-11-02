def solution():
    """Krystiana owns an apartment building. The rooms on the first floor cost $15 per month and the rooms on the 2nd floor cost $20 per month. The rooms on the third floor cost twice as much as the rooms on the first floor, but only two rooms are occupied. If each floor has 3 rooms, how much does Krystiana earn every month?"""
    first_floor_rooms = 3
    second_floor_rooms = 3
    third_floor_rooms = 3
    
    first_floor_cost = 15 * first_floor_rooms
    second_floor_cost = 20 * second_floor_rooms
    third_floor_cost = (2 * 15) * 2
    
    total_earned = first_floor_cost + second_floor_cost + third_floor_cost
    result = total_earned
    return result

print(solution())