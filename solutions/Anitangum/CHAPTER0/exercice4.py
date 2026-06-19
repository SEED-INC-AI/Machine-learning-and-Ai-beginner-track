text = "  Hello, World! HELLO  "

text = text.strip()
print(text)  # "Hello, World! HELLO"

text = text.lower()
print(text)  # "hello, world! hello"

count = text.count("hello")
print(count)  # 2

text = text.replace("world", "python")
print(text)  # "hello, python! hello"
