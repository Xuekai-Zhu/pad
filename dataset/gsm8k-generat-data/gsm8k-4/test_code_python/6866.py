def solution():
    """At the duck park, there are 25 mallard ducks and ten less than twice as many geese as ducks.
    Then, a small flock of 4 ducks arrived at the park and joined the birds already there.
    If five less than 15 geese leave the park, how many more geese than ducks remain at the park?"""
    
    # Define the number of mallard ducks
    mallard_ducks = 25

    # Define the number of geese
    geese = (2*mallard_ducks) - 10

    # Update the number of ducks after the arrival of a small flock
    mallard_ducks += 4

    # Calculate the number of geese after the arrival of the small flock
    geese += (2*4) - 10

    # Calculate the number of geese that remain after five fewer leave the park
    geese -= 5

    # Calculate the difference between the number of geese and ducks
    difference = geese - mallard_ducks

    result = difference
    return result

print(solution())