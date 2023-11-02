def solution():
    """If Ruby is 2 centimeters shorter than Pablo.  Pablo is 70 centimeters taller than Charlene.  Janet is 62 centimeters tall and Charlene is twice that tall.  How tall is Ruby?"""
    # Define Charlene's height
    charlene_height = 62 * 2

    # Calculate Pablo's height
    pablo_height = charlene_height + 70

    # Calculate Ruby's height
    ruby_height = pablo_height - 2

    # Display Ruby's height
    result = ruby_height
    return result

print(solution())