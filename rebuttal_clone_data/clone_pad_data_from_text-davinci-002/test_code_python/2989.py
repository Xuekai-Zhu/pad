def solution():
    stamps = 13
    matchbooks = 5
    matches_per_book = 24
    stamps_per_book = 1
    books_traded = matchbooks * stamps_per_book
    matches_traded = books_traded * matches_per_book
    stamps_left = stamps + matches_traded
    result = stamps_left
    return result

print(solution())