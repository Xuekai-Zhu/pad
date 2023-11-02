def solution():
    # Let's call the number of clownfish and blowfish in their own tank "x"
    x = 26
    
    # Since there are an equal number of clownfish and blowfish in the aquarium, we can say that the total number of fish is 2x
    total_fish = 100
    
    # We know that 26 blowfish stayed in their own tank, so the rest (x-26) went to the display tank
    # And we know that an equal number of clownfish joined them, so the total number of fish in the display tank is (x-26) + (x-26) = 2(x-26)
    display_fish = 2*(x-26)
    
    # We also know that a third of the clownfish in the display tank swam back to their own tank, so (2/3) of them stayed in the display tank
    # Therefore, the number of clownfish in the display tank is (2/3)*(x-26)
    clownfish_display = (2/3)*(x-26)
    result = clownfish_display
    return result

print(solution())