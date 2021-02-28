def collatz_length(num):
	count = 1

	while num != 1:
		count += 1
		if num % 2 == 0:
			num /= 2
		else:
			num = 3 * num + 1

	return count

# print(collatz_length(13)) => 10

maxlen = 10
num = 0

for i in range(2, 1000000):
	length = collatz_length(i)
	# print(str(i) + " has length " + str(length))
	if length > maxlen:
		maxlen = length
		num = i
		print("new max: " + str(i) + " has length " + str(length))

print(num) # => 837799
