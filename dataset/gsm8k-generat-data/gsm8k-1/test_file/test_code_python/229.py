def solution():
    """There are 36 penguins sunbathing in the snow. One-third of them jump in and swim in the ocean. Another one-third go inside the cave to eat their dinner. How many penguins are still left sunbathing?"""
    total_penguins = 36
    penguins_swimming = total_penguins / 3
    penguins_eating = total_penguins / 3
    penguins_sunbathing = total_penguins - penguins_swimming - penguins_eating
    result = penguins_sunbathing
    return result

print(solution())