def solution():
    """Among the career home run leaders for MLB, Hank Aaron has 175 fewer than twice the number that Dave Winfield has. Hank Aaron hit 755 home runs. How many home runs did Dave Winfield hit in his career?"""
    hank_aaron_hr = 755
    dave_winfield_hr = (hank_aaron_hr - 175) / 2
    result = dave_winfield_hr
    return result

print(solution())