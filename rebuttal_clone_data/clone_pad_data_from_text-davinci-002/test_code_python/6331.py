def solution():
    pages_read_per_minute_anna = 1
    pages_read_per_minute_carole = 0.5 * pages_read_per_minute_anna
    pages_read_per_minute_brianna = 2 * pages_read_per_minute_anna
    pages_read_per_minute_total = pages_read_per_minute_anna + pages_read_per_minute_carole + pages_read_per_minute_brianna
    pages_read_in_x_minutes = 100 / pages_read_per_minute_total
    result = pages_read_in_x_minutes
    return result

print(solution())