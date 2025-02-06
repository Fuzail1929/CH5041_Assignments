def rand_uniform(n):
    x0 = 1  
    y0 = 1.78
    a = 16807 
    m = (1 << 31) - 1 
    count = 0  

    for _ in range(n):
        x0 = (a * x0) % m  
        y0 = (a * y0) % m  
        
        x = x0 / (1.0*m) 
        y = y0 /(1.0*m) 

        if (x - 0.5) *(x - 0.5) + (y - 0.5) *(y - 0.5) <= 0.25:
            count += 1.0 
    count/=n;
    print(count*4.0)


n = int(input())
rand_uniform(n)
