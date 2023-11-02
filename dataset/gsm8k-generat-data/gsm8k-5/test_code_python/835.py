def solution():
    # Calculate the number of cars in the back parking lot
    back_lot = 2 * 100  # two times more vehicles in the back than in the front

    # Calculate the total number of cars parked before the play
    before_play = 100 + back_lot

    # Calculate the number of cars parked after the play
    after_play = 700

    # Calculate the number of cars that parked during the play
    parked_during_play = after_play - before_play
    result = parked_during_play
    return result

print(solution())