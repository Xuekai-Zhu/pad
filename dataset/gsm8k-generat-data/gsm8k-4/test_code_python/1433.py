def solution():
    """Among the career home run leaders for MLB, Hank Aaron has 175 fewer than twice the number that Dave Winfield has.
    Hank Aaron hit 755 home runs. How many home runs did Dave Winfield hit in his career?"""
    
    # Hank Aaron's number of home runs
    hank_aaron_hr = 755
    
    # Equation to determine Dave Winfield's number of home runs
    # 2 * dave_winfield_hr - 175 = hank_aaron_hr
    dave_winfield_hr = (hank_aaron_hr + 175) / 2
    
    result = dave_winfield_hr
    return result

print(solution())