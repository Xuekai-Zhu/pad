def solution():
    """If Jim has 20 apples, and Jane has 60 apples, and Jerry has 40 apples, how many times can Jim's number of apples fit into the average amount of apples for a person in the group?"""
    total_apples = 20 + 60 + 40
    num_people = 3
    avg_apples_per_person = total_apples / num_people
    num_times_jims_apples_fit = avg_apples_per_person / 20
    result = num_times_jims_apples_fit
    return result

print(solution())