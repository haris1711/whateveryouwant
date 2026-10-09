def foo(bar):
    return bar + 1


def make_numbers(N):
    ret = []
    
    for i in range(0, N):
        j = i
        
        if N%4 == 0:
            print(10)
            j += 5
            input("next ?")

            q = j ** 2
        
        ret.append([
            j * 10,
            q
        ])

    return ret

print(make_numbers(10))