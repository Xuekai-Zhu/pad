def solution():
    # Calculate the total number of spoons from the babies
    baby_spoons = 4 * 3

    # Add the baby spoons and the decorative spoons to get the total number of old spoons
    old_spoons = baby_spoons + 2

    # Add the old spoons to the new set of cutlery to get the total number of spoons
    total_spoons = old_spoons + 10

    # Calculate the total number of teaspoons
    total_teaspoons = 15

    # Add the total number of spoons and teaspoons to get the final answer
    result = total_spoons + total_teaspoons
    return result

print(solution())