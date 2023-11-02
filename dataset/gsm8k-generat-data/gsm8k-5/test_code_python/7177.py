def solution():
    gecko_count = 5  # There are 5 geckos on the window
    gecko_daily_insects = 6  # Each gecko eats 6 insects per day

    # Calculate the number of insects eaten by the geckos in one day
    gecko_total_insects = gecko_count * gecko_daily_insects

    lizard_count = 3  # There are 3 lizards that eat twice as much as the geckos

    # Calculate the number of insects eaten by the lizards in one day
    lizard_total_insects = lizard_count * (2 * gecko_daily_insects)

    # Calculate the total number of insects eaten
    total_insects = gecko_total_insects + lizard_total_insects
    result = total_insects
    return result

print(solution())