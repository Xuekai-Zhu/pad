def solution():
    """Finn watches 11 tadpoles swimming in the pond. Suddenly he sees 6 of them come out of hiding from under a lily pad, then he sees 2 of them hide under a rock. How many tadpoles can Finn see in the pond now?"""
    tadpoles_initial = 11
    tadpoles_show = 6
    tadpoles_hide = 2
    tadpoles_total = tadpoles_initial + tadpoles_show - tadpoles_hide
    result = tadpoles_total
    return result

print(solution())