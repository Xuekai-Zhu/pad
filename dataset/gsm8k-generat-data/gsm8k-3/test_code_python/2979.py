def solution():
    """Barbeck has two times as many guitars as Steve, but Davey has three times as many guitars as Barbeck. If there are 27 guitars altogether, how many guitars does Davey have?"""
    # Let's assume Steve has x guitars
    # Barbeck has two times as many guitars as Steve: 2x
    # Davey has three times as many guitars as Barbeck: 3(2x) = 6x
    # We know that there are 27 guitars altogether:
    # x + 2x + 6x = 27
    # Solving for x:
    x = 3

    # Now we can calculate how many guitars Davey has:
    davey_guitars = 6 * x

    # Display the number of guitars Davey has
    result = davey_guitars
    return result

print(solution())