# Exercise 1.1: Create a list of squares for numbers 1-20
# TODO: Use list comprehension
sqr_list = [x**2 for x in range(1,20)]
print(f'sqr_list: {sqr_list}')

# Exercise 1.2: Filter even numbers from 0-50
# TODO: Use list comprehension with condition
even_list = [x for x in range(1,50,2)]
print(f'even_list: {even_list}' )

# Exercise 1.3: Convert list of words to uppercase
words = ["python", "data", "science", "machine", "learning"]
# TODO: Use list comprehension
upper_words = [word.upper() for word in words]
print(f'upper_words: {upper_words}')

# Exercise 1.4: Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# TODO: Use nested list comprehension
flatten_list = [item for sublist in nested for item in sublist]
print(f'flatten_list: {flatten_list}')

# Exercise 1.5: Create pairs of (number, square, cube)
# TODO: Use list comprehension for numbers 1-10
pairs = [(num,num**2,num**3) for num in range(1,10)]
print(f'pairs: {pairs}')

# Exercise 2.1: Count word frequencies in a sentence
text = "the quick brown fox jumps over the lazy dog the fox is quick"
# TODO: Create dict with word frequencies using dict comprehension
dict_text = dict(text.split())
print(dict_text)

# Exercise 2.2: Create word-to-index mapping
# From exercise 2.1 frequencies, create bidirectional mapping
# TODO: word_to_index and index_to_word dictionaries

# Exercise 2.3: Sort frequencies by count (descending)
# TODO: Return list of tuples (word, count) sorted by count

# Exercise 2.4: Top N words
# TODO: Function to return top N most frequent words

# Exercise 2.5: Merge multiple word frequency dictionaries
freq_dict1 = {'apple': 3, 'banana': 2}
freq_dict2 = {'apple': 1, 'cherry': 4}
freq_dict3 = {'banana': 1, 'date': 2}
# TODO: Merge all three dicts accumulating counts