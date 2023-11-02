def solution():
     books_assigned = 89
     books_read_mcgregor = 34
     books_read_floyd = 32
     books_unread = books_assigned - books_read_mcgregor - books_read_floyd
     result = books_unread
     return result

print(solution())