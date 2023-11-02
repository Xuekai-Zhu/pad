def solution():
    """Farmer Brown raises emus, large birds. His flock has a total of 60 heads and legs. How many emus are in his flock?"""
    # We can use a system of linear equations to solve this problem
    # Let e be the number of emus and l be the number of legs per emu
    # Then we have:
    # e + l = 60  (total number of heads and legs)
    # 2e + 4l = 2 * (e + l)  (total number of legs, since each emu has 2 legs and each head also counts as a leg)
    # Solving for e in the first equation gives e = 60 - l
    # Substituting into the second equation and simplifying gives:
    # 2(60 - l) + 4l = 120
    # 120 - 2l + 4l = 120
    # 2l = 0
    # l = 0
    # This would imply that there are no legs or emus, which doesn't make sense
    # The only other solution is when l = 2 and e = 58
    # We can check that this solution satisfies both equations
    num_legs = 60 * 2
    num_emus = 58
    total_legs = num_emus * 2
    if total_legs == num_legs:
        return num_emus
    else:
        return "No solution"

print(solution())