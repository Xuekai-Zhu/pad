def solution():
    """Caleb and his dad went fishing at the lake. Caleb caught 2 trouts and his dad caught three times as much as Caleb. How many more trouts did his dad catch compared to Caleb?"""
    # Define the number of trouts Caleb caught
    caleb_trouts = 2

    # Calculate the number of trouts Caleb's dad caught
    dads_trouts = caleb_trouts * 3

    # Calculate the difference in the number of trouts caught by Caleb's dad and Caleb
    diff_trouts = dads_trouts - caleb_trouts

    # return the result
    result = diff_trouts
    return result

print(solution())