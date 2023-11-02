def solution():
    """Krystiana owns an apartment building. The rooms on the first floor cost $15 per month and the rooms on the 2nd floor cost $20 per month.
    The rooms on the third floor cost twice as much as the rooms on the first floor, but only two rooms are occupied. If each floor has 3 rooms,
    how much does Krystiana earn every month?"""
    
    # Define the prices for each floor
    first_price = 15
    second_price = 20
    third_price = first_price * 2

    # Define the number of rooms on each floor
    rooms_per_floor = 3

    # Calculate the total monthly earnings for each floor
    first_floor_earnings = first_price * rooms_per_floor
    second_floor_earnings = second_price * rooms_per_floor
    third_floor_earnings = third_price * 2
    
    # Calculate the total monthly earnings for the building
    total_earnings = first_floor_earnings + second_floor_earnings + third_floor_earnings
    
    result = total_earnings
    return result

print(solution())