def solution():
    # Create a list to store the remaining fraction of popsicles after each melt
    remaining_popsicles = [1]

    # Simulate the melting process and populate the list
    for i in range(5):
        remaining_popsicles.append(remaining_popsicles[-1] / 2)

    # Calculate the ratio of the last remaining popsicle to the first
    ratio = remaining_popsicles[-1] / remaining_popsicles[0]

    result = ratio
    return result

print(solution())