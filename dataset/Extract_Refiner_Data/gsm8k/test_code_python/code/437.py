def solution():
    
    # Define the number of packs of each color of bead purchased
    red_packs = 1
    clear_packs = 2
    blue_packs = 3
    red_packs = 4

    # Calculate the total number of beads purchased by Elizabeth and Margareth
    elizabeth_beads = (red_packs + clear_packs) * 20
    margareth_beads = (blue_packs + red_packs) * 20

    # Calculate the total number of beads purchased by both sisters
    total_beads = elizabeth_beads + margareth_beads

    # Calculate the difference in the number of beads purchased by each sister
    difference = total_beads - 1

    # Display the difference in the number of beads purchased by each sister
    result = difference
    return result

print(solution())