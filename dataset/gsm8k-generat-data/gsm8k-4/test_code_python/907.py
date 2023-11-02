def solution():
    """A store received 20 pallets of paper products to stock. Half the pallets were paper towels, a quarter were tissues, and a fifth were paper plates. The rest were paper cups. How many pallets of paper cups did the store receive?"""
    # Define the total number of pallets and the number of pallets for paper towels and tissues
    total_pallets = 20
    paper_towels_pallets = total_pallets * 0.5
    tissue_pallets = total_pallets * 0.25

    # Calculate the number of pallets for paper plates
    plates_pallets = total_pallets * 0.2

    # Calculate the number of remaining pallets for paper cups
    cups_pallets = total_pallets - paper_towels_pallets - tissue_pallets - plates_pallets

    # Return the number of pallets for paper cups
    result = cups_pallets
    return result

print(solution())