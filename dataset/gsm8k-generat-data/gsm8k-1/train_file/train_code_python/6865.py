def solution():
    """At the duck park, there are 25 mallard ducks and ten less than twice as many geese as ducks. Then, a small flock of 4 ducks arrived at the park and joined the birds already there. If five less than 15 geese leave the park, how many more geese than ducks remain at the park?"""
    ducks = 25
    geese = 2*ducks - 10
    total_birds = ducks + geese + 4
    geese_left = 15 - 5
    total_geese = geese - geese_left
    remaining_geese = total_geese - ducks
    result = remaining_geese
    return result

print(solution())