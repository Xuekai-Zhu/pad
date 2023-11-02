def solution():
    # Calculate the number of torn pages
    torn_pages = 150 - (5 * 25)

    # Calculate the number of comics with torn pages
    torn_comics = torn_pages // 25

    # Calculate the total number of comics
    total_comics = 5 + torn_comics

    result = total_comics
    return result

print(solution())