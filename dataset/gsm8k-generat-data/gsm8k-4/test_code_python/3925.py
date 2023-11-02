def solution():
    """Jenny is working on a school project. She spends 10 hours doing research for the project and 2 hours writing a proposal. If she has 20 hours total to work on the project, how many hours does she have left to write her report?"""
    # Define the total hours spent on research and proposal
    research_hours = 10
    proposal_hours = 2

    # Define the total hours available for the project
    total_hours = 20

    # Calculate the remaining hours for writing the report
    remaining_hours = total_hours - research_hours - proposal_hours

    # return the result
    result = remaining_hours
    return result

print(solution())