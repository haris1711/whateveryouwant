def foo(bar):
    return bar + 1


def make_numbers(N):
    ret = []
    
    for i in range(0, N):
        j = i
        
        if N%2 == 0:
            j += 1
        
        ret.append(j * 2)

    return ret

print(make_numbers(10))