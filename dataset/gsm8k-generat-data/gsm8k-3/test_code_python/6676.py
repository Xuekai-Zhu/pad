def solution():
    """A museum has eight different wings displaying four times as many artifacts as paintings displayed. Three of the wings are dedicated to paintings. The artifacts are divided evenly among the remaining wings. One painting is so large it takes up an entire wing, and the other two wings house 12 smaller paintings each. How many artifacts are in each artifact wing?"""
    # Define the number of paintings in the painting wings
    large_painting = 1
    small_paintings = 2 * 12
    total_paintings = large_painting + small_paintings

    # Calculate the number of artifacts in each artifact wing
    artifacts_per_wing = 4 * total_paintings / 5

    # Display the number of artifacts in each artifact wing
    result = artifacts_per_wing
    return result

print(solution())