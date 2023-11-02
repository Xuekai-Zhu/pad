def solution():
    """Sedrach has 13 apple pies. If every apple pie can be quickly divided into halves and every half an apple pie can be split into 5 bite-size samples, how many people can taste Sedrach's apple pie if he divides them all into bite-size samples?"""
    # Define the number of apple pies
    apple_pies = 13

    # Calculate the number of halves of each apple pie
    apple_pie_halves = apple_pies * 2

    # Calculate the total number of bite-size samples
    bite_size_samples = apple_pie_halves * 5

    # Display the number of people who can taste the apple pies
    result = bite_size_samples
    return result

print(solution())