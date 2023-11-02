def solution():
    # Calculate the number of novels
    num_novels = 0.65 * 120

    # Calculate the number of comic books
    num_comics = 120 - num_novels - 18

    # Calculate the percentage of comic books
    percent_comics = (num_comics / 120) * 100

    result = percent_comics
    return result

print(solution())