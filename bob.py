def foo(bar):
    return bar + 1


def make_numbers(N):
    ret = []
    
    for i in range(0, N):
        j = i
        
        if N%2 == 0:
            j += 2
            print(j)
            
        ret.append(j * 3)

    return ret


def super_cool_something(nums):
    ret = 1
    
    for i in nums:
        print(i)

        if i%3==0:
            ret *= i-2

    return ret


print(super_cool_something([10, 11, 20, 4]))