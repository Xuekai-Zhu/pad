def solution():
    pages_read_Sunday = 43
    pages_read_Monday = 65
    pages_read_Tuesday = 28
    pages_read_Thursday = 70
    pages_read_Friday = 56
    pages_read_Wednesday = 0
    pages_read_goal = 50
    remaining_pages = pages_read_goal - (pages_read_Sunday + pages_read_Monday + pages_read_Tuesday + pages_read_Wednesday + pages_read_Thursday + pages_read_Friday)
    result = remaining_pages
    
    return result

print(solution())