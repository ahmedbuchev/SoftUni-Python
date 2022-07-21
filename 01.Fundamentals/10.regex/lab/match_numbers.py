import re

text = input()
pattern = f"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result = re.finditer(pattern, text)

for match in result:
    print(match.group(), end=" ")
