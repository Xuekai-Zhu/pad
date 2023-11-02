def solution():
    pages_per_comic = 25
    total_pages = 150
    num_intact_comics = 5

    # Calculate the number of torn comics by dividing the total number of pages by the pages per comic
    num_torn_comics = total_pages // pages_per_comic

    # Calculate the total number of comics by adding the number of torn and intact comics
    total_comics = num_torn_comics + num_intact_comics
    result = total_comics
    return result

print(solution())