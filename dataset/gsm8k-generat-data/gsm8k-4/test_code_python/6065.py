def solution():
    """Anna has 50 pencils and Harry has twice the number of Anna’s Pencils but he lost 19 of them. How many pencils are left with Harry?"""
    # Define the initial number of pencils
    anna_pencils = 50

    # Calculate the number of pencils Harry had initially (twice Anna's pencils)
    harry_pencils = anna_pencils * 2

    # Subtract the lost pencils from Harry's total
    harry_pencils -= 19

    result = harry_pencils
    return result

print(solution())