def solution():
    # Calculate the total number of snails eaten by the snail kites in 5 days
    total_snails = 3 + (3+2) + (5+2) + (7+2) + (9+2)  # on the first day it ate 3 snails, then 2 more each day until the fifth day
    result = total_snails
    return result

print(solution())