def solution():
    # Define the ratio of Amy's age to Jeremy's age
    amy_to_jeremy_ratio = 1/3

    # Define the ratio of Chris's age to Amy's age
    chris_to_amy_ratio = 2

    # Calculate the total age of the three people
    total_age = 132

    # Set up a system of equations using the ratios and total age
    # Let a = Amy's age, j = Jeremy's age, and c = Chris's age
    # Then we have:
    # a + j + c = total_age
    # a = (1/3)j
    # c = 2a
    # Substitute the second and third equations into the first equation to get:
    # (1/3)j + j + 2(1/3)j = total_age
    # Simplify and solve for j:
    j = total_age / (1 + 1/3 + 2*(1/3))
    
    result = j
    return result

print(solution())