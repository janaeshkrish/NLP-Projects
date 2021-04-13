import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
bat
mat
'''


emails = """
Janaesh@gmail.com
jan.123@gmail.org
JAn-234@my-work.net
"""
pattern = re.compile(r'[A-Za-z.0-9-]+@[A-Za-z-]+[a-zA-Z]+')

#matches = pattern.finditer(emails)

matches = pattern.findall(emails)#list of words


matches = pattern.match(emails)#matches only the begining of the string


matches = pattern.search(emails)#searches and display only one words
print(matches)

# for i in matches:
#     print(i)