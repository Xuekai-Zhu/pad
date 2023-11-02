def solution():
    # Let the distance between the Nile Delta and the River Nile be D, and let Paul's speed be S
    # Then, we know that D/S = 4, i.e., Paul takes 4 hours to walk from his home to the Nile Delta
    # On the return journey, the speed of the alligators is (S/7) since there are 7 alligators including Paul
    # We also know that D/(S/7) = 4 + 2, i.e., it takes 2 more hours to travel from the Nile Delta to the River Nile
    # Solving these equations, we can find S and thus compute the total time the alligators walked

    D = symbols('D')
    S = symbols('S')
    equations = [
        Eq(D/S, 4),
        Eq(D/(S/7), 6)
    ]
    sol = solve(equations, (D, S))

    distance = sol[D]
    paul_speed = sol[S]
    alligators_speed = paul_speed / 7

    time_paul = distance / paul_speed
    time_alligators = distance / alligators_speed

    total_time = time_paul + time_alligators
    result = round(total_time, 2)
    return result

print(solution())