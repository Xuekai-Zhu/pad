def solution():
    """Paityn has 20 red hats and 24 blue hats. Her friend Zola has 4/5 times as many red hats as she has and twice the number of blue hats. If they combine all the hats together and share them equally between themselves, calculate the number of hats each gets."""
    # Define the initial number of hats for Paityn
    paityn_red_hats = 20
    paityn_blue_hats = 24

    # Calculate the number of hats for Zola
    zola_red_hats = int((4/5) * paityn_red_hats)
    zola_blue_hats = 2 * paityn_blue_hats

    # Calculate the total number of hats
    total_hats = paityn_red_hats + paityn_blue_hats + zola_red_hats + zola_blue_hats

    # Calculate the number of hats each person gets if they share equally
    hats_per_person = total_hats // 2

    # Return the result
    result = hats_per_person
    return result

print(solution())