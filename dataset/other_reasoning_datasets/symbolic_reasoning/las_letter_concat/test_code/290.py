def solution():
    s = "Rahul Praveen Isaiah Elsie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())