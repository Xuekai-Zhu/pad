def solution():
    """Susie's pet lizard Moe takes 10 seconds to eat 40 pieces of cuttlebone each day. How long would it take Moe to eat 800 pieces?"""
    # Calculate how many batches of 40 pieces Moe needs to eat to reach 800
    batches = 800 / 40

    # Calculate how long it takes Moe to eat one batch
    time_per_batch = 10

    # Calculate how long it would take Moe to eat all 800 pieces
    total_time = batches * time_per_batch

    # Display the result in seconds
    result = total_time
    return result

print(solution())