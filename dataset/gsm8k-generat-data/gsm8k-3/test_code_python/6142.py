def solution():
    """Krystiana owns an apartment building. The rooms on the first floor cost $15 per month and the rooms on the 2nd floor cost $20 per month. The rooms on the third floor cost twice as much as the rooms on the first floor, but only two rooms are occupied. If each floor has 3 rooms, how much does Krystiana earn every month?"""
    # Define the cost of each type of room
    FIRST_FLOOR_PRICE = 15
    SECOND_FLOOR_PRICE = 20
    THIRD_FLOOR_PRICE = 2 * FIRST_FLOOR_PRICE

    # Define the number of rooms on each floor
    NUM_ROOMS_PER_FLOOR = 3

    # Calculate the total monthly earnings from the first and second floors
    first_floor_earnings = FIRST_FLOOR_PRICE * NUM_ROOMS_PER_FLOOR
    second_floor_earnings = SECOND_FLOOR_PRICE * NUM_ROOMS_PER_FLOOR
    total_earnings = first_floor_earnings + second_floor_earnings

    # Calculate the earnings from the two rooms on the third floor
    third_floor_earnings = THIRD_FLOOR_PRICE * 2

    # Add the earnings from the third floor to the total earnings
    total_earnings += third_floor_earnings

    # Display the total monthly earnings
    result = total_earnings
    return result

print(solution())