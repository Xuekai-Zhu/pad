def solution():
    """If Jim has 20 apples, and Jane has 60 apples, and Jerry has 40 apples, how many times can Jim's number of apples fit into the average amount of apples for a person in the group?"""
    # Calculate the total number of apples in the group
    total_apples = 20 + 60 + 40

    # Calculate the average number of apples per person
    average_apples = total_apples / 3

    # Calculate how many times Jim's number of apples fits into the average
    times_fit = average_apples // 20

    # Display the result
    result = times_fit
    return result

print(solution())