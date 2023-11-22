def solution():
    
    # Define the weight of each comic book and toy
    COMIC_BOOK_WEIGHT = 0.25
    TYS_WEIGHT = 0.5

    # Define the number of comic books to remove
    num_comic_books = 30

    # Calculate the total weight of the comic books
    total_comic_weight = num_comic_books * COMIC_BOOK_WEIGHT

    # Calculate the weight of the toys to remove
    total_ty_weight = total_comic_weight * TYS_WEIGHT

    # Calculate the number of toys to remove
    num_toys = 15 / TYS_WEIGHT

    # Display the number of toys to remove
    result = num_toys
    return result

print(solution())