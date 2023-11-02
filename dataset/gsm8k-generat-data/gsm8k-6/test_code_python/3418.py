def solution():
    # Calculate the total number of stamps in Stella's album
    rows_per_page = 5
    stamps_per_row_page1 = 30
    pages_with_30_stamps = 10
    pages_with_50_stamps = 50 - pages_with_30_stamps

    # Calculate the total number of stamps on pages with 30 stamps per row
    stamps_on_pages_with_30_stamps = rows_per_page * stamps_per_row_page1 * pages_with_30_stamps

    # Calculate the total number of stamps on pages with 50 stamps per page
    stamps_on_pages_with_50_stamps = 50 * pages_with_50_stamps

    # Calculate the total number of stamps in Stella's album
    total_stamps = stamps_on_pages_with_30_stamps + stamps_on_pages_with_50_stamps
    result = total_stamps
    return result

print(solution())