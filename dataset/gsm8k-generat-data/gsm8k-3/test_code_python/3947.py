def solution():
    """Bill has 6 times as many nuts as Harry, and Harry has twice as many nuts as Sue. If Sue has 48 nuts, how many do Bill and Harry have combined?"""
    # Define the number of nuts Sue has
    sue_nuts = 48

    # Calculate the number of nuts Harry has
    harry_nuts = sue_nuts * 2

    # Calculate the number of nuts Bill has
    bill_nuts = harry_nuts * 6

    # Calculate the total number of nuts Bill and Harry have combined
    total_nuts = harry_nuts + bill_nuts

    # Display the total number of nuts
    result = total_nuts
    return result

print(solution())