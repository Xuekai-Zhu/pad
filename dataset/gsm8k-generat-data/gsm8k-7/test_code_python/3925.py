def solution():
    research_time = 10
    proposal_time = 2
    total_time = 20

    # Calculate the total time spent on research and the proposal
    total_spent = research_time + proposal_time

    # Calculate the time left to write the report
    remaining_time = total_time - total_spent

    result = remaining_time
    return result

print(solution())