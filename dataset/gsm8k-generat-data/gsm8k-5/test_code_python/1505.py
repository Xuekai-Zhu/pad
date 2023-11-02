def solution():
    lambs = 6  # Mary starts with 6 lambs
    lambs_with_babies = 2 * 2  # 2 of the lambs had 2 babies each
    lambs = lambs + lambs_with_babies  # Mary now has a total of 10 lambs
    lambs = lambs - 3  # Mary trades 3 lambs for 1 goat, so she has 7 lambs left
    lambs = lambs + 7  # Mary finds 7 extra lambs in the field
    result = lambs
    return result

print(solution())