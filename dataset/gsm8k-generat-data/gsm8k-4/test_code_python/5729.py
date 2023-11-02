def solution():
    """Milly is making feather boas for her dance team. Each flamingo has 20 tail feathers, and it's only safe to pluck 25% of their tail feathers at one time. If Milly needs to make 12 boas, and each boa has 200 feathers, how many flamingoes does she need to harvest?"""
    # Define the number of tail feathers per flamingo and the safe plucking rate
    TAIL_FEATHERS_PER_FLAMINGO = 20
    SAFE_PLUCKING_RATE = 0.25

    # Define the number of boas to make and the number of feathers per boa
    NUM_BOAS = 12
    FEATHERS_PER_BOA = 200

    # Calculate the total number of feathers needed
    total_feathers = NUM_BOAS * FEATHERS_PER_BOA

    # Calculate the number of feathers that can be safely plucked from one flamingo
    safe_feathers_per_flamingo = TAIL_FEATHERS_PER_FLAMINGO * SAFE_PLUCKING_RATE

    # Calculate the number of flamingos needed to harvest enough feathers
    flamingos_needed = total_feathers / safe_feathers_per_flamingo

    # Round up to the nearest integer
    flamingos_needed = int(math.ceil(flamingos_needed))

    result = flamingos_needed
    return result

print(solution())