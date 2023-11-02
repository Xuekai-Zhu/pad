def solution():
    num_papers = 296
    num_hours = 8

    # Calculate the rate at which Ms. Alice can grade papers
    rate = num_papers / num_hours

    # Calculate the number of papers she can grade in 11 hours
    num_papers_11_hours = rate * 11
    result = num_papers_11_hours
    return result

print(solution())