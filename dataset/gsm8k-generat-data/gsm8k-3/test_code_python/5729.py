def solution():
    """Milly is making feather boas for her dance team. Each flamingo has 20 tail feathers, and it's only safe to pluck 25% of their tail feathers at one time. If Milly needs to make 12 boas, and each boa has 200 feathers, how many flamingoes does she need to harvest?"""
    # Define the number of feathers needed for each boa
    BOA_FEATHERS = 200

    # Define the percentage of feathers that can be safely harvested from each flamingo
    SAFE_PERCENT = 25

    # Define the number of tail feathers on each flamingo
    FLAMINGO_FEATHERS = 20

    # Define the number of boas Milly needs to make
    NUM_BOAS = 12

    # Calculate the total number of feathers needed
    total_feathers = BOA_FEATHERS * NUM_BOAS

    # Calculate the number of flamingos needed to harvest enough feathers
    flamingos_needed = (total_feathers / (FLAMINGO_FEATHERS * (SAFE_PERCENT/100))) + 1

    # Display the number of flamingos needed
    result = int(flamingos_needed)
    return result

print(solution())