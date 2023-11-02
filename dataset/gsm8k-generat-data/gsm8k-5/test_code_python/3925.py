def solution():
    total_project_time = 20  # Jenny has 20 hours to work on the project
    research_time = 10  # Jenny spent 10 hours doing research
    proposal_time = 2  # Jenny spent 2 hours writing a proposal

    # Calculate the remaining time for Jenny to write her report
    report_time = total_project_time - research_time - proposal_time
    result = report_time
    return result

print(solution())