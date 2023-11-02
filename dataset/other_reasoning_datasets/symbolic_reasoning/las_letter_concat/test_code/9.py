def solution():
    s = "Beatriz Gillian Coco Vivian"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())