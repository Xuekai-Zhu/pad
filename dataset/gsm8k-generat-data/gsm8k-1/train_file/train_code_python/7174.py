def solution():
    """A frog pond has five frogs living in it. Some frogs laid eggs, and now there are three times as many tadpoles growing into more frogs as there are frogs. Two-thirds of the tadpoles will survive to maturity as frogs. The pond can only sustain eight frogs. How many frogs will have to find a new pond when the tadpoles grow up?"""
    initial_frog_count = 5
    tadpole_count = initial_frog_count * 3
    mature_frog_count = int(tadpole_count * (2/3))
    final_frog_count = initial_frog_count + mature_frog_count
    frogs_to_move = final_frog_count - 8
    result = frogs_to_move
    return result

print(solution())