def solution():
    # Define how many eBook readers Anna bought
    anna_ebook_readers = 50

    # Calculate how many eBook readers John bought
    john_ebook_readers = anna_ebook_readers - 15

    # Calculate how many eBook readers they have after John loses 3
    total_ebook_readers = anna_ebook_readers + john_ebook_readers - 3

    result = total_ebook_readers
    return result

print(solution())