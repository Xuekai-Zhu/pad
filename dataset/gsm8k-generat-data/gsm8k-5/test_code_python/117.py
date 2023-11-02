def solution():
    # Let n be the number of clownfish and blowfish in the aquarium
    # Then n/2 is the number of each individual fish
    # After 26 blowfish stay in their own tank, (n/2 - 26) blowfish swim into the display tank
    # An equal number of clownfish (n/2 - 26) join the blowfish in the display tank
    # But then (1/3)(n/2 - 26) clownfish swim back into their own tank
    # So the total number of fish in the aquarium is:
    n = 2 * ((n/2 - 26) + (n/2 - 26) + (1/3)(n/2 - 26))

    # We know that the total number of fish is 100, so we can solve for n
    n = 60

    # The number of clownfish in the display tank is equal to the number of clownfish that joined the blowfish
    # in the display tank, minus the number of clownfish that swam back into their own tank
    clownfish_in_display = (n/2 - 26) - (1/3)(n/2 - 26)
    result = clownfish_in_display
    return result

print(solution())