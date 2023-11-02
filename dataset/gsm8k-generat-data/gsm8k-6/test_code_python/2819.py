def solution():
    # Calculate the total number of book chapters that Brian read
    chapters_read = 20 + 2*15 + 0.5*(20 + 2*15)  # one book with 20 chapters, two books with 15 chapters each, and one book with half the chapters of the previous three books put together
    result = chapters_read
    return result

print(solution())