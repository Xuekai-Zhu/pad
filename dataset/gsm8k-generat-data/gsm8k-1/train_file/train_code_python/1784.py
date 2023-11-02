def solution():
    """Angeli had 90 assorted candies. One-third of the candies were lollipops and the rest were candy canes.
    She then shared the lollipops equally among the boys such that each boy received 3.
    She then shared the candy canes equally among the girls such that each received 2.
    How many boys and girls were given altogether?"""
    total_candies = 90
    lollipops = total_candies / 3
    candy_canes = total_candies - lollipops

    boys = lollipops / 3
    girls = candy_canes / 2
    
    total_people = boys + girls
    
    result = total_people
    return result

print(solution())