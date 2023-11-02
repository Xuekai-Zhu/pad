def solution():
    s = "Sue Cassandra Cody Cali"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())