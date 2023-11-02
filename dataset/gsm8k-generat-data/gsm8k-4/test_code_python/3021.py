def solution():
    """Jessica wrote a long letter to her aunt and needed to put stamps on it to mail it. She used eight pieces of paper that weigh 1/5 of an ounce each, and her envelope weighs 2/5 of an ounce. She needed one stamp per ounce. How many stamps did Jessica need to mail her letter?"""
    # Define the weight of one piece of paper
    paper_weight = 1/5 

    # Calculate the total weight of the papers
    total_paper_weight = 8 * paper_weight

    # Add the weight of the envelope
    total_weight = total_paper_weight + 2/5

    # Calculate the number of stamps needed
    stamps_needed = int(total_weight)

    # return the result
    result = stamps_needed
    return result

print(solution())