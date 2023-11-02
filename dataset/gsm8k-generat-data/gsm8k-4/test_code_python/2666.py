def solution():
    """If Jim has 20 apples, and Jane has 60 apples, and Jerry has 40 apples, how many times can Jim's number of apples fit into the average amount of apples for a person in the group?"""
    # Calculate the total number of apples
    total_apples = 20 + 60 + 40

    # Calculate the average number of apples per person
    avg_apples = total_apples / 3

    # Calculate the number of times Jim's number of apples can fit into the average
    times_fit = avg_apples // 20

    result = int(times_fit)
    return result

print(solution())