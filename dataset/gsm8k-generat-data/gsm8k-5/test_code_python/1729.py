def solution():
    num_roaches = 12  # Calvin has 12 giant roaches in his collection
    num_scorpions = 3  # Calvin has 3 scorpions in his collection
    num_crickets = num_roaches / 2  # Calvin has half as many crickets as roaches
    num_caterpillars = 2 * num_scorpions  # Calvin has twice as many caterpillars as scorpions

    # Calculate the total number of insects in Calvin's collection
    total_insects = num_roaches + num_scorpions + num_crickets + num_caterpillars
    result = total_insects
    return result

print(solution())