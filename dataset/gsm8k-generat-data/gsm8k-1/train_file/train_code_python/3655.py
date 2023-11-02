def solution():
    """A hand-crank pencil sharpener can sharpen one pencil every forty-five seconds. An electric version can sharpen one in twenty seconds. How many more pencils can the electric sharpener sharpen than the hand-crank sharpener in six minutes?"""
    hand_crank_time = 45 # seconds
    electric_time = 20 # seconds
    total_time = 6 * 60 # seconds in 6 minutes
    pencils_hand_crank = total_time // hand_crank_time
    pencils_electric = total_time // electric_time
    difference = pencils_electric - pencils_hand_crank
    result = difference
    return result

print(solution())