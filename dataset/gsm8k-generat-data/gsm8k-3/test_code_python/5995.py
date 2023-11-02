def solution():
    """Mary has 300 sheep and Bob has double the number of sheep as Mary plus another 35. How many sheep must Mary buy to have 69 fewer sheep than Bob?"""
    # Define the number of Mary's sheep and Bob's sheep
    mary_sheep = 300
    bob_sheep = (mary_sheep * 2) + 35

    # Calculate how many sheep Mary needs to buy
    needed_sheep = (bob_sheep - 69) - mary_sheep

    # Display the number of sheep Mary needs to buy
    result = needed_sheep
    return result

print(solution())