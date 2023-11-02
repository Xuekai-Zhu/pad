def solution():
    """Erica is getting dessert at a pie buffet where all the pies are the same size. She takes 1/5 of an apple pie and 3/4 of a cherry pie. What fraction of a whole pie did Erica take, expressed as a percentage?"""
    # Define the fractions of apple pie and cherry pie taken by Erica
    apple_fraction = 1/5
    cherry_fraction = 3/4

    # Calculate the total fraction of a whole pie taken by Erica
    total_fraction = apple_fraction + cherry_fraction

    # Convert the fraction to a percentage
    percentage = total_fraction * 100

    result = percentage
    return result

print(solution())