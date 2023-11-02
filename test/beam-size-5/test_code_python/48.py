def solution():
    
    # Define the weight of each type of book
    COMIC_BOOK_WEIGHT = 1/4
    TOY_WEIGHT = 1/2

    # Define the number of comic books to remove
    num_comic_books = 30

    # Calculate the total weight of the comic books to remove
    total_comic_weight = num_comic_books * COMIC_BOOK_WEIGHT

    # Calculate the remaining weight of the toys
    remaining_weight = 15 - total_comic_weight

    # Calculate the number of toys to remove
    num_toys = remaining_weight / TOY_WEIGHT

    # Display the number of toys to remove
    result = num_toys
    return result

print(solution())