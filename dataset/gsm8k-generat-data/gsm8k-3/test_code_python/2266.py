def solution():
    """Haley has 5 more necklaces than Jason. Josh has half the number of necklaces as Jason. If Haley has 25 necklaces, how many more necklaces does Haley have than Josh?"""
    # Let's assume that Jason has J number of necklaces
    # Haley has 5 more necklaces than Jason, so H = J + 5
    # Josh has half the number of necklaces as Jason, so Jsh = 0.5J

    # We know that Haley has 25 necklaces
    H = 25

    # Using H = J + 5, we can solve for J
    J = H - 5

    # Using Jsh = 0.5J, we can solve for Jsh
    Jsh = 0.5 * J

    # Calculate the difference in number of necklaces between Haley and Josh
    diff = H - Jsh

    # Display the result
    result = diff
    return result

print(solution())