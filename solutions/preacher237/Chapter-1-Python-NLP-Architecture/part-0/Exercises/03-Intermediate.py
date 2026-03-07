#Exercise 1: List Operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
max_V = max(numbers)
min_V = min(numbers)
count = numbers.count(1)
numbers = [x for x in numbers if x != 1]
average = sum(numbers) / len(numbers)

#Exercise 2: Slicing Practice
data = [10, 20, 30, 40, 50, 60, 70]
print(data[1])
print(data[-3:])
print(data[::-1])

#Exercise 3: Data Normalization
scores = [55, 65, 75, 85, 95]
