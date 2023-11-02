def solution():
    """Police officer A patrols 36 streets in 4 hours. His colleague, officer B, patrols 55 streets in 5 hours. How many streets will both officers patrol in one hour?"""
    # calculate officer A's patrol rate
    a_rate = 36 / 4

    # calculate officer B's patrol rate
    b_rate = 55 / 5

    # calculate the combined patrol rate
    combined_rate = a_rate + b_rate

    # calculate the number of streets both officers will patrol in one hour
    streets_per_hour = combined_rate / 2

    result = streets_per_hour
    return result

print(solution())