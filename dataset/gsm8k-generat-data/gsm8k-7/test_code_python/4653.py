def solution():
    # Let's use variables to represent the number of cans brought in by each person
    # We'll use m for Mark, j for Jaydon, and r for Rachel
    m = 0
    j = 0
    r = 0

    # We know that the total number of cans is 135, so we can set up an equation
    # m + j + r = 135

    # We also know that Mark brings in 4 times as many cans as Jaydon
    # m = 4j

    # And we know that Jaydon brings in 5 more than twice the amount of cans that Rachel brought in
    # j = 2r + 5

    # We can substitute the second equation into the first equation to get rid of j
    # m + (2r + 5) + r = 135
    # m + 3r + 5 = 135
    # m + 3r = 130

    # We can substitute the first equation into the third equation to get rid of j and r
    # m = 4(2r + 5)
    # m = 8r + 20

    # Now we have two equations with two variables
    # m + 3r = 130
    # m = 8r + 20

    # We can substitute the second equation into the first equation to get rid of m
    # (8r + 20) + 3r = 130
    # 11r = 110
    # r = 10

    # Now that we know r, we can use the second equation to solve for m
    # m = 8r + 20
    # m = 8(10) + 20
    # m = 100

    result = m
    return result

print(solution())