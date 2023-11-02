def solution():
    """ Mary sees three breeding balls with 8 snakes each and 6 additional pairs of snakes. How many snakes did she see total? """
    
    # Define the number of snakes in each breeding ball
    snakes_per_ball = 8
    
    # Calculate the total number of snakes in the breeding balls
    total_snakes_in_balls = 3 * snakes_per_ball
    
    # Define the number of snakes in each pair
    snakes_per_pair = 2
    
    # Calculate the total number of snakes in the additional pairs
    total_snakes_in_pairs = 6 * snakes_per_pair
    
    # Calculate the total number of snakes seen
    total_snakes = total_snakes_in_balls + total_snakes_in_pairs
    
    # Display the total number of snakes seen
    result = total_snakes
    return result

print(solution())