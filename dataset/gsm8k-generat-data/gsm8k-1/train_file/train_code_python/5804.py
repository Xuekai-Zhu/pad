def solution():
    """Youngsville had a population of 684 people. The town had a growth spurt and the population increased by 25% then they witnessed that 40% of the population moved away. What is the current population?"""
    initial_pop = 684
    growth_percent = 25
    growth_amount = initial_pop * (growth_percent / 100)
    pop_after_growth = initial_pop + growth_amount
    moved_percent = 40
    moved_amount = pop_after_growth * (moved_percent / 100)
    current_pop = pop_after_growth - moved_amount
    result = current_pop
    return result

print(solution())