def solution():
    """Bianca worked for 12.5 hours last weekend. Celeste worked for twice that amount of time and McClain worked 8.5 hours less than Celeste. How many minutes did the 3 people work in total?"""
    # Define the number of hours worked by Bianca
    hours_bianca = 12.5

    # Define the number of hours worked by Celeste
    hours_celeste = 2 * hours_bianca

    # Define the number of hours worked by McClain
    hours_mcclain = hours_celeste - 8.5

    # Calculate the total number of minutes worked by all three people
    total_minutes = (hours_bianca + hours_celeste + hours_mcclain) * 60

    # return the result
    result = total_minutes
    return result

print(solution())