def solution():
    
    
    
    jade_for_giraffe = 120
    num_giraffes = 1920 // jade_for_giraffe
    
    
    giraffe_price = 150
    giraffe_revenue = giraffe_price * num_giraffes
    
    
    jade_for_elephant = jade_for_giraffe * 2
    
    
    num_elephants = 1920 // jade_for_elephant
    
    
    elephant_price = 350
    elephant_revenue = elephant_price * num_elephants
    
    
    difference = elephant_revenue - giraffe_revenue
    
    return difference

print(solution())