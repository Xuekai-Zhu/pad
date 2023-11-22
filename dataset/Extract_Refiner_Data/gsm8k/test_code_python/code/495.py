def solution():
    
    # Define the cost of the first venue and the second venue
    venue_cost = 200
    venue_food_cost = 5

    # Calculate the total cost of the two venues at the second venue
    total_cost = venue_cost + (25 * venue_food_cost)

    # Calculate the number of guests needed to be equal in cost
    num_guests = total_cost / venue_cost

    # Display the number of guests needed
    result = num_guests
    return result

print(solution())