def solution():
    """Every year in January, Natalia, the librarian, tidies up the books. She has 145 novels, 271 comics, 419 documentaries, and 209 albums to store. She wants to put these in crates that can hold 9 items. How many crates will Natalia use?"""
    # Define the number of items in each category
    NOVELS = 145
    COMICS = 271
    DOCUMENTARIES = 419
    ALBUMS = 209

    # Calculate the total number of items
    total_items = NOVELS + COMICS + DOCUMENTARIES + ALBUMS

    # Calculate the number of crates needed
    crates_needed = total_items // 9

    # Display the number of crates needed
    result = crates_needed
    return result

print(solution())