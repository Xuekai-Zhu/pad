def solution():
    rob_time = 1  # It takes 1 hour for Rob to get to the park
    mark_time = 3 * rob_time  # It takes Mark three times as long as Rob to get to the park
    total_time = rob_time + mark_time  # They both need to arrive at the same time

    rob_departure_time = 11  # Rob leaves his home at 11 a.m.
    mark_departure_time = rob_departure_time - (mark_time - rob_time)  # Calculate the time Mark needs to leave his home
    result = mark_departure_time
    return result

print(solution())