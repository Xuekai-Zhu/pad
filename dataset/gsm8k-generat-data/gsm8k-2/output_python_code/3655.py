def solution():
    """A hand-crank pencil sharpener can sharpen one pencil every forty-five seconds. An electric version can sharpen one in twenty seconds. How many more pencils can the electric sharpener sharpen than the hand-crank sharpener in six minutes?"""
    hand_crank_time = 45
    electric_time = 20
    hand_crank_pencils = (6 * 60) / hand_crank_time
    electric_pencils = (6 * 60) / electric_time
    difference = electric_pencils - hand_crank_pencils
    result = difference
    return result

print(solution())