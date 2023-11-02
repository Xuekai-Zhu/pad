def solution():
    jordan_catch = 4
    perry_catch = jordan_catch * 2
    total_catch = jordan_catch + perry_catch
    lost_catch = total_catch / 4

    # Calculate the remaining number of fish
    remaining_catch = total_catch - lost_catch
    result = remaining_catch
    return result

print(solution())