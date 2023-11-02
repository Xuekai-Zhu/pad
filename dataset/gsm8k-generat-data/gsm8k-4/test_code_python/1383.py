def solution():
    """Issac has to buy pens and pencils for the upcoming school year. Issac buys 108 writing utensils total. He buys 12 more than 5 times the number of pencils than pens. How many pens did Issac buy?"""
    # Define the total number of writing utensils
    total_utensils = 108

    # Let the number of pens be x
    x = None

    # Calculate the number of pencils
    y = (total_utensils - 12) / 6

    # Calculate the number of pens
    x = total_utensils - y

    # Return the result
    result = x
    return result

print(solution())