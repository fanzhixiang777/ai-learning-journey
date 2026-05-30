with open('madlibs.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
adjective = input('Enter an adjective:\n')
content = content.replace('ADJECTIVE', adjective)
NOUN1 = input('Enter a noun:\n')
content = content.replace('NOUN', NOUN1, 1)
NOUN2 = input('Enter another noun:\n')
content = content.replace('NOUN', NOUN2, 1)
VERB = input('Enter a verb:\n')
content = content.replace('VERB', VERB)
with open('madlibs_result.txt', 'w', encoding='UTF-8') as f:
    f.write(content)
print(content)