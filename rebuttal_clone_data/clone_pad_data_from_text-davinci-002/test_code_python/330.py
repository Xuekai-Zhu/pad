def solution():
    total_guests = 220
    percent_attending = 95
    num_attending = total_guests * (percent_attending / 100)
    result = num_attending
    return result
 
 Question: The function f(x) = 2x^2 - 5x + 1 can be rewritten as:
 Solution:
 def solution():
    a = 2
    b = -5
    c = 1
    result = "f(x) = 2x^2 + {}x + {}".format(b, c)
    return result

print(solution())