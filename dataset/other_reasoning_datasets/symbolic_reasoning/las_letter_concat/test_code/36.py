def solution():
    s = "Kennedy Ginny Iliana Sky"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())