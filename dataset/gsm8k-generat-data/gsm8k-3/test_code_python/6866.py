def solution():
    """At the duck park, there are 25 mallard ducks and ten less than twice as many geese as ducks.  Then, a small flock of 4 ducks arrived at the park and joined the birds already there.  If five less than 15 geese leave the park, how many more geese than ducks remain at the park?"""
    # Calculate the initial number of geese
    initial_geese = 2 * 25 - 10
    
    # Add the four ducks that arrived
    total_ducks = 25 + 4
    
    # Subtract the ducks that left
    remaining_geese = initial_geese - (15 - 5)
    
    # Calculate the difference between geese and ducks
    difference = remaining_geese - total_ducks
    
    # Display the result
    result = difference
    return result

print(solution())