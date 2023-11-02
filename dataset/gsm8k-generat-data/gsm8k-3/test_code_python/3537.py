def solution():
    """Jennie makes quilts. She can make 7 quilts with 21 yards of material. How many yards of material would be required to make 12 quilts?"""
    # Define the number of quilts and yards of material Jennie can make with 1 yard
    QUILTS_PER_YARD = 7 / 21

    # Define the number of quilts to be made
    quilts_to_make = 12

    # Calculate the yards of material required
    yards_required = quilts_to_make / QUILTS_PER_YARD

    # Display the yards of material required
    result = yards_required
    return result

print(solution())