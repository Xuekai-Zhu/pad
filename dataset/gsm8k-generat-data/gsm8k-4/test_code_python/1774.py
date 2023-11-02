def solution():
    """Sedrach has 13 apple pies. If every apple pie can be quickly divided into halves and every half an apple pie can be split into 5 bite-size samples, how many people can taste Sedrach's apple pie if he divides them all into bite-size samples?"""
    # Define the number of apple pies
    num_pies = 13

    # Calculate the total number of bite-size samples
    total_samples = (num_pies * 2) * 5

    # Display the number of people who can taste Sedrach's apple pie
    result = total_samples
    return result

print(solution())