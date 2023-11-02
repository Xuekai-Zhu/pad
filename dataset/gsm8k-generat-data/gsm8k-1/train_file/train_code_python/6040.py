def solution():
    """Every year in January, Natalia, the librarian, tidies up the books. She has 145 novels, 271 comics, 419 documentaries, and 209 albums to store. She wants to put these in crates that can hold 9 items. How many crates will Natalia use?"""
    total_books = 145 + 271 + 419 + 209
    crates_needed = total_books // 9
    if total_books % 9 != 0:
        crates_needed += 1
    result = crates_needed
    return result

print(solution())