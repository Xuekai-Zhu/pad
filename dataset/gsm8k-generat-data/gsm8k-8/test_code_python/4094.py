def solution():
    # Define Lidia's collection as 4 times larger than Susan's collection
    lidia_collection = 4 * susan_collection

    # Define the total number of books as the sum of Lidia and Susan's collections
    total_books = 3000

    # Use algebra to solve for Susan's collection size
    susan_collection = (total_books / 5)

    # Return the size of Susan's collection
    result = susan_collection
    return result

print(solution())