def solution():
    """At the duck park, there are 25 mallard ducks and ten less than twice as many geese as ducks.
    Then, a small flock of 4 ducks arrived at the park and joined the birds already there.
    If five less than 15 geese leave the park, how many more geese than ducks remain at the park?"""
    ducks = 25 + 4  # 29 ducks total
    geese = (2 * 25) - 10  # 40 geese total
    geese -= (15 - 5)  # 30 geese remaining after 10 leave 
    difference = geese - ducks  # calculate difference between geese and ducks
    result = difference
    return result

print(solution())