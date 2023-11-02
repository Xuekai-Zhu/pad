def solution(l, w):
    rectangle_area = l * w
    square_area = w**2
    difference = rectangle_area - square_area
    result = difference
    return result

print(solution())