def create_rs(start, end, steps):
    z = y = x = start
    q = []
    
    while y <= end:
        while z <= end:
            q.append([x, y, z])
            z += steps
        z = 0
        y += steps
        
    return q

create_rs(0, 2, 1)