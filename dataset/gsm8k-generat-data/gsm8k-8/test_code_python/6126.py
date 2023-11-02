def solution():
    # Calculate the total number of pencils Paul made during the week
    total_pencils_made = 100 * 5

    # Calculate the total number of pencils Paul had at the beginning of the week
    beginning_stock = 80

    # Calculate the total number of pencils Paul sold during the week
    pencils_sold = 350

    # Calculate the total number of pencils Paul had at the end of the week
    end_stock = beginning_stock + total_pencils_made - pencils_sold
    result = end_stock
    return result

print(solution())