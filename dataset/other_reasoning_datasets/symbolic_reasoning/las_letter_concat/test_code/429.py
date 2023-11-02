def solution():
    s = "Miguel Angel Saul Brady Darryl"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())