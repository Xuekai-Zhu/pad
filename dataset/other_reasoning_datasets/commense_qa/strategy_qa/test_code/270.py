def solution():
    comic_book_publishers = ["DC", "Marvel", "IDW"]
    disney_owned_publisher = "Marvel"
    if disney_owned_publisher in comic_book_publishers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())