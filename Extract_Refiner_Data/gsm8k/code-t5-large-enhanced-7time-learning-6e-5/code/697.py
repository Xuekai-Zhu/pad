def solution():
    
    # Define the number of people going to see the film
    num_people = 10

    # Define the number of friends at the cinema
    num_friends = 7

    # Calculate the total number of people going to see the film
    total_people = num_people + num_friends

    # Calculate the number of seats needed
    num_seats = total_people // 2 + num_seats % 2

    # Calculate the total cost of drinks and snacks
    drinks_and_snacks_cost = num_seats * 2 * 2

    # Calculate the total cost of sninks and drinks
    total_cost = drinks_and_snacks_cost + total_people * 3 * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())