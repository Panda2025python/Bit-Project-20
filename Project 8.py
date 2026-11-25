numbers = [-4, 6, 2, 0, 0, 1, 1]
index = 2
left_slice = numbers[:index]
right_slice = numbers[index + 1:]
print(left_slice, sum(left_slice))
print(right_slice, sum(right_slice))

for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])
    print(i, left_sum, right_sum)
    if left_sum == right_sum:
        print("Equilibrium:", i, numbers[i])

values = window_sum = 0
for i in range(len(values)):
    window_sum += values[i]
    print(values[:i + 1], window_sum)

target = 10
found = False
for start in range(len(values)):
    current_sum = 0
    for end in range(start, len(values)):
        current_sum += values[end]
        if current_sum == target:
            print(values[start:end + 1], start, end)
            found = True

if not found:
    print("Not found")
