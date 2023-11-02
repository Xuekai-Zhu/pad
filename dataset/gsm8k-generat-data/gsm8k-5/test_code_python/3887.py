def solution():
    total_distance = 70  # The two dogs walk a total of 70 miles a week
    dog1_distance = 2 * 7  # The first dog walks 2 miles a day for 7 days a week
    dog2_distance = total_distance - dog1_distance  # The second dog walks the remaining distance

    # Calculate the average distance the second dog walks per day
    dog2_avg_distance = dog2_distance / (7 - 1)  # There are 7 days in a week, but we already counted the first dog's distance

    result = dog2_avg_distance
    return result

print(solution())