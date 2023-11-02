def solution():
    # Calculate the total number of gems purchased
    total_gems = 250 * 100

    # Calculate the bonus gems received
    bonus_gems = 0.2 * total_gems

    # Calculate the total number of gems received
    total_gems_received = total_gems + bonus_gems
    result = total_gems_received
    return result

print(solution())