def solution():
    perimeter = 100
    width = perimeter / 10  # Since the total of length and width equals to 1/2 of the perimeter, width is half of the perimeter divided by 10
    length = width * 4
    result = length
    return result

print(solution())