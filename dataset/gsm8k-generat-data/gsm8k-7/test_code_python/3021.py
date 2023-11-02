def solution():
    weight_per_paper = 1/5
    num_papers = 8
    envelope_weight = 2/5

    # Calculate the total weight of the papers
    total_paper_weight = weight_per_paper * num_papers

    # Calculate the total weight of the letter
    total_weight = total_paper_weight + envelope_weight

    # Calculate the number of stamps needed
    num_stamps = total_weight
    result = num_stamps
    return result

print(solution())