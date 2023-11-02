def solution():
    """Richard, Jerry, and Robert are going to share 60 cherries. If Robert has 30 cherries, and has 10 more than Richard, how many more cherries does Robert have than Jerry?"""
    total_cherries = 60
    robert_cherries = 30
    richard_cherries = robert_cherries - 10
    jerry_cherries = total_cherries - robert_cherries - richard_cherries
    robert_more_cherries = robert_cherries - jerry_cherries
    result = robert_more_cherries
    return result

print(solution())