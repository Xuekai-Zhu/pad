def solution():
    """During a day at the farm, Annie picked eight pints of blueberries. Kathryn picked two pints more than Annie, and Ben picked three pints fewer than Kathryn. How many pints, in total, did the three pick together?"""
    # Define the number of pints picked by Annie
    annie_pints = 8

    # Calculate the number of pints picked by Kathryn
    kathryn_pints = annie_pints + 2

    # Calculate the number of pints picked by Ben
    ben_pints = kathryn_pints - 3

    # Calculate the total number of pints picked by the three
    total_pints = annie_pints + kathryn_pints + ben_pints

    # Return the result
    result = total_pints
    return result

print(solution())