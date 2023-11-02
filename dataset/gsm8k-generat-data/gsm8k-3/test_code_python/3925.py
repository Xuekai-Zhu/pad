def solution():
    """Jenny is working on a school project. She spends 10 hours doing research for the project and 2 hours writing a proposal. If she has 20 hours total to work on the project, how many hours does she have left to write her report?"""
    # Define the time spent on research and proposal
    research_time = 10
    proposal_time = 2

    # Define the total time for the project
    total_time = 20

    # Calculate the time left for report writing
    report_time = total_time - research_time - proposal_time

    # Display the time left for report writing
    result = report_time
    return result

print(solution())