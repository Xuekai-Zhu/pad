def solution():
    """A water tower that serves four neighborhoods around it holds 1200 barrels of water and is filled to the top each week. If one neighborhood uses 150 barrels of water in a week, the second neighborhood uses twice as many barrels of water as the first neighborhood in a week, and the third neighborhood uses one hundred more barrels of water than the second neighborhood in a week, how many barrels are left for the fourth neighborhood?"""
    # Define the total number of barrels of water in the water tower
    total_barrels = 1200

    # Deduct the number of barrels used by the first neighborhood
    total_barrels -= 150

    # Calculate the number of barrels used by the second neighborhood
    neighborhood_two = 150 * 2

    # Calculate the number of barrels used by the third neighborhood
    neighborhood_three = neighborhood_two + 100

    # Deduct the total number of barrels used by the first three neighborhoods
    total_barrels -= neighborhood_two + neighborhood_three

    # The remaining barrels are for the fourth neighborhood
    result = total_barrels
    return result

print(solution())