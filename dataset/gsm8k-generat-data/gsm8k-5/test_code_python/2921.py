def solution():
    # Let's assume the number of times Martin rings the big bell is "x"
    # Then the number of times he rings the small bell would be (1/3)x + 4

    total_rings = 52  # Martin rings both bells a combined total of 52 times

    # We can set up an equation based on the information above:
    # x + (1/3)x + 4 = total_rings

    # Simplifying the equation, we get:
    # (4/3)x = total_rings - 4
    # x = 3(total_rings - 4)/4  (solving for x)

    # Calculate the number of times Martin rings the big bell
    big_bell_rings = 3 * (total_rings - 4) / 4
    result = big_bell_rings
    return result

print(solution())