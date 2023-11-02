def solution():
    # Define the relevant facts
    rosalind_franklin_contribution = True
    understanding_of_DNA_structure = True
    genome_sequencing_dependent_on_DNA_structure = True
    # Check if Rosalind Franklin's contribution led to genome sequencing
    if rosalind_franklin_contribution and understanding_of_DNA_structure and genome_sequencing_dependent_on_DNA_structure:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())