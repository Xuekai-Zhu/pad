def solution():
    # Define Sammy's pickle slice consumption
    sammy_slices = 15

    # Define Tammy's pickle slice consumption
    tammy_slices = sammy_slices * 2

    # Calculate Ron's pickle slice consumption, 20% fewer than Tammy
    ron_slices = tammy_slices - (0.2 * tammy_slices)

    result = ron_slices
    return result

print(solution())