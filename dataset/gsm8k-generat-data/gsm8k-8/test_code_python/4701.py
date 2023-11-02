def solution():
    # Calculate the total cost for Kath and her siblings
    num_people = 3
    before_6pm_cost = 8 - 3
    kath_and_siblings_cost = num_people * before_6pm_cost

    # Calculate the total cost for Kath's friends
    num_friends = 3
    regular_cost = 8
    friends_cost = num_friends * regular_cost

    # Calculate the total cost for all of them
    total_cost = kath_and_siblings_cost + friends_cost
    result = total_cost
    return result

print(solution())