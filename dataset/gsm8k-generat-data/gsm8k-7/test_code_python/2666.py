def solution():
    jim_apples = 20
    jane_apples = 60
    jerry_apples = 40

    # Calculate the total number of apples in the group
    total_apples = jim_apples + jane_apples + jerry_apples

    # Calculate the average number of apples for a person in the group
    avg_apples = total_apples / 3

    # Calculate how many times Jim's number of apples can fit into the average amount
    times_into_avg = avg_apples // jim_apples
    result = times_into_avg
    return result

print(solution())