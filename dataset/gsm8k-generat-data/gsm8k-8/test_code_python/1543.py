def solution():
    # Calculate the number of sit-ups Nathan can do
    nathan_situps = 2 * 20

    # Calculate the combined number of sit-ups Ken and Nathan can do
    ken_nathan_situps = 20 + nathan_situps

    # Calculate Bob's number of sit-ups
    bob_situps = 0.5 * ken_nathan_situps

    # Calculate the difference between Bob and Ken's sit-ups
    diff_situps = bob_situps - 20
    result = diff_situps
    return result

print(solution())