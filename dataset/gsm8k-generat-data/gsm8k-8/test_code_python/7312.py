def solution():
    # Define the number of pages drawn in the first and second months
    first_month_pages = x
    second_month_pages = x

    # Calculate the number of pages drawn in the third month
    third_month_pages = first_month_pages + 4

    # Calculate the total number of pages drawn in the three months
    total_pages = first_month_pages + second_month_pages + third_month_pages

    # Use algebra to solve for the value of x (number of pages in the first month)
    x = (total_pages - 220) / 2

    result = x
    return result

print(solution())