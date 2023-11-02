def solution():
    """Bianca worked for 12.5 hours last weekend. Celeste worked for twice that amount of time and McClain worked 8.5 hours less than Celeste. How many minutes did the 3 people work in total?"""
    # Define the number of hours worked by Bianca
    bianca_hours = 12.5

    # Calculate the number of hours worked by Celeste
    celeste_hours = bianca_hours * 2

    # Calculate the number of hours worked by McClain
    mcclain_hours = celeste_hours - 8.5

    # Calculate the total number of minutes worked by all three people
    total_minutes = (bianca_hours + celeste_hours + mcclain_hours) * 60

    # Display the total number of minutes worked
    result = total_minutes
    return result

print(solution())