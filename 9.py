for i in range(1, 1000): # will be smallest
    for j in range(1, 1000-i): # should be second smallest
        k = 1000 - i - j
        if i**2 + j**2 == k**2:
            print(i*j*k)
            break
    else:
        continue
    break