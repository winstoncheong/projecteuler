
def is_palindrome(num):
    return str(num) == str(num)[::-1]


# Diagonal traversal...
# (999, 999), (999, 998), (999, 997)
# (998, 999), (998, 998), (998, 997)
# (997, 999), (997, 998), (997, 997)

# (0,0) (1,0) (1,1)

for i in range(999):
    for j in range(i+1):
        # print(i,j,999-i+j, 999-j)
        val = (999-i+j) * (999-j)
        if is_palindrome(val):
            print(val)
            break
    else:
        continue
    break
