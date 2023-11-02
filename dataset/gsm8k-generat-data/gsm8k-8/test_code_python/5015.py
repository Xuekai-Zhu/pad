def solution():
    # Let's call the speed at which Jack cycles "x"
    # Let's also call the time it takes for Jack to go from the store to his friend "t"
    # Based on the information in the question, we can set up the following equations:
    # 20/x = 2t  -> it takes Jack twice as long to go from his home to the store as it takes to go from the store to his friend
    # 50/x + 50/x = t  -> Jack and Peter cycle back to the store together, so their combined distance from the store is 50 miles

    # Solving for t in the first equation:
    t = 10/x

    # Substituting t into the second equation and solving for x:
    x = 25

    # Now that we know Jack's speed, we can calculate the total distance he cycled today:
    distance_to_store = 20
    distance_to_friend = 50
    distance_back_to_store = 50
    total_distance = distance_to_store + distance_to_friend + distance_back_to_store

    result = total_distance
    return result

print(solution())