def solution():
    # Assume that Mariel is walking x dogs
    # The other dog walker is also walking x dogs
    # Each dog has 4 legs
    # So the total number of legs would be 4*(2x + 3)

    total_legs = 4*(2*x + 3)

    # We know that there are 36 legs tangled up in leashes
    # So, we can set up an equation to find x

    4*(2*x + 3) = 36
    x = (36/4 - 3)/2

    # Simplifying the equation, we get:

    x = 3

    # Mariel is walking 3 dogs
    result = 3
    return result

print(solution())