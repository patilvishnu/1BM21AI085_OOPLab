def largest_element(l1):
    num1=0
    for num in l1:
        if num>num1:
            num1=num
        else:
            continue
    return(num1)

l1=[-11,-12,3,4,62]
largest_element(l1)
