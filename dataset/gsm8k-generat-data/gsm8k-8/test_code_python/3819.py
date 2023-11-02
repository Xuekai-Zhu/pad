def solution():
    # Define the initial number of necklaces
    initial_necklaces = 50

    # Calculate the number of unbroken beads collected
    unbroken_beads = 3 * 12

    # Calculate the number of necklaces after collecting unbroken beads
    new_necklaces = initial_necklaces - 3 + unbroken_beads

    # Calculate the number of necklaces after buying new ones
    new_total_necklaces = new_necklaces + 5

    # Calculate the final number of necklaces after giving some away
    final_necklaces = new_total_necklaces - 15
    result = final_necklaces
    return result

print(solution())