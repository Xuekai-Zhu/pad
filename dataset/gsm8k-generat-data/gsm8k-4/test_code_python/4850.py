def solution():
    """While bird watching, Gabrielle saw 5 robins, 4 cardinals, and 3 blue jays.
    Chase saw 2 robins, 3 blue jays, and 5 cardinals. How many more birds, in percentage,
    did Gabrielle see than Chase?"""
    # Define the number of birds seen by Gabrielle
    gabrielle_robins = 5
    gabrielle_cardinals = 4
    gabrielle_bluejays = 3

    # Define the number of birds seen by Chase
    chase_robins = 2
    chase_bluejays = 3
    chase_cardinals = 5

    # Calculate the total number of birds seen by Gabrielle and Chase
    gabrielle_total = gabrielle_robins + gabrielle_cardinals + gabrielle_bluejays
    chase_total = chase_robins + chase_bluejays + chase_cardinals

    # Calculate the difference in the number of birds seen and convert to percentage
    diff_percentage = ((gabrielle_total - chase_total) / chase_total) * 100

    # return the result
    result = round(diff_percentage)
    return result

print(solution())