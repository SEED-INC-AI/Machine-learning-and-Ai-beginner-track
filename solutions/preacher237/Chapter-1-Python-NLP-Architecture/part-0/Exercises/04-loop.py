# Exercise 1: Sum Calculator
# Calculate sum of numbers 1 to 100
num =[x for x in range(1,100)]
sum =0
for i in num:
    sum +=i
print(sum)

# Exercise 2: List Processing
# Given a list of scores, print each with a pass/fail indicator

scores = [45, 78, 92, 65, 88, 52, 95]
for i in scores:
    if i >=70:
        print("PASS")
    else:
        print("FAIL")

# Exercise 3: Pattern Generation
# Create a 5x5 multiplication table using nested loops
for i in range(1,6):
    for j in range(1,6):
        print(i*j, end=" ")
    print()

# Exercise 4: Word Counter
# Count occurrences of each word
text = "the quick brown fox jumps over the lazy dog the"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Exercise 5: ML Data Normalization
raw_data = [100, 50, 75, 25, 90, 60]
min_val = min(raw_data)
max_val = max(raw_data)
normalized = [(x - min_val) / (max_val - min_val) for x in raw_data]
print(normalized)