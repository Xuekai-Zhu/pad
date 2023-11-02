def solution():
    """Every year in January, Natalia, the librarian, tidies up the books. She has 145 novels, 271 comics, 419 documentaries, and 209 albums to store. She wants to put these in crates that can hold 9 items. How many crates will Natalia use?"""
    # Define the number of books in each category
    novels = 145
    comics = 271
    documentaries = 419
    albums = 209

    # Calculate the total number of items
    total_items = novels + comics + documentaries + albums

    # Calculate the number of crates needed to store all items
    crates = total_items // 9

    # Add one additional crate if there are any remaining items
    if total_items % 9 != 0:
        crates += 1

    # return the result
    result = crates
    return result

print(solution())