n = int(raw_input())

sum = 0
while n > 0:
	sum += n % 10
	n = n / 10

print(sum)