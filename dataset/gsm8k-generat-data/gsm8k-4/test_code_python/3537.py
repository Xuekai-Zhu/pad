def solution():
    """Jennie makes quilts. She can make 7 quilts with 21 yards of material. How many yards of material would be required to make 12 quilts?"""
    # Define the number of quilts and yards of material needed for the initial scenario
    initial_quilts = 7
    initial_yards = 21

    # Calculate the ratio of quilts to yards of material
    ratio = initial_quilts / initial_yards

    # Use the ratio to calculate the number of yards needed for 12 quilts
    quilts_needed = 12
    yards_needed = quilts_needed / ratio

    # Return the result
    result = yards_needed
    return result

print(solution())