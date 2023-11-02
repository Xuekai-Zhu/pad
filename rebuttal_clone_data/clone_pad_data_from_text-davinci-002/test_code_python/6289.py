def solution():
    applications_sent_per_state = 200
    other_states_applications_sent = applications_sent_per_state * 2
    total_applications_sent = applications_sent_per_state + other_states_applications_sent
    result = total_applications_sent
    return result

print(solution())