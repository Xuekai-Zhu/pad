def solution():
    """To make a cherry pie, Veronica needs 3 pounds of pitted cherries. There are 80 single cherries in one pound of cherries. It takes 10 minutes to pit 20 cherries. How many hours will it take Veronica to pit all the cherries?"""
    cherries_per_pound = 80
    pounds_of_cherries = 3
    total_cherries = cherries_per_pound * pounds_of_cherries
    pitted_cherries = total_cherries
    cherries_pitted_per_round = 20
    time_per_round = 10
    while pitted_cherries > 0:
        pitted_cherries -= cherries_pitted_per_round
        if pitted_cherries < 0:
            time_per_cherries_pitted = (pitted_cherries + cherries_pitted_per_round) / cherries_pitted_per_round * time_per_round
        else:
            time_per_cherries_pitted = time_per_round
        time_to_pit_all_cherries += time_per_cherries_pitted

    result = time_to_pit_all_cherries / 60
    return result

print(solution())