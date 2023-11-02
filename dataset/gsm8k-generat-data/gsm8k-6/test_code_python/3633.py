def solution():
    # Calculate the number of sips Marcy takes to drink the whole bottle of water
    total_sips = (2 * 1000) / 40  # 2-liter bottle has 2,000 ml of water, each sip is 40 ml

    # Calculate the total time taken to drink the whole bottle of water
    total_time = total_sips * 5  # Marcy takes a sip every 5 minutes

    result = total_time
    return result

print(solution())