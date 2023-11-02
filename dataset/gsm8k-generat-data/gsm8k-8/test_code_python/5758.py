def solution():
    # Billy picks 36 dandelions
    billy_picks = 36

    # George picks 1/3 as many as Billy
    george_picks = billy_picks / 3

    # They each pick 10 more each after seeing the pile
    billy_picks += 10
    george_picks += 10

    # Calculate the average of their total picks
    total_picks = billy_picks + george_picks
    average_picks = total_picks / 2
    result = average_picks
    return result

print(solution())