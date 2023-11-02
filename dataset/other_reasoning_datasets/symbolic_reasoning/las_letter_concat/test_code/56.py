def solution():
    s = "Vicente Dayana Kasey Lin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())