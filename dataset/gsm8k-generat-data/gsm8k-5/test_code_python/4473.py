def solution():
    tony = 23
    dean = 12
    breanna = 17

    # Calculate the number of books Tony and Dean read together
    tony_and_dean = 3

    # Calculate the number of books all three read together
    all_three = 1

    # Calculate the total number of different books read
    total_books = tony + dean + breanna - tony_and_dean*2 - all_three

    result = total_books
    return result

print(solution())