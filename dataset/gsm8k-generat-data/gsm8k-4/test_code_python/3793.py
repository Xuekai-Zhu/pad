def solution():
    """Max is planning a vacation for 8 people. The Airbnb rental costs $3200. They also plan on renting a car that will cost $800. If they plan on splitting the costs equally, how much will each person’s share be?"""
    # Define the total cost of the rental and the car
    total_cost = 3200 + 800

    # Divide the total cost equally among the 8 people
    share_per_person = total_cost / 8

    # Return the result
    result = share_per_person
    return result

print(solution())