import sys

print('hello world')

characters = [ 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
for x in characters:
    sys.stdout.write(x)

sorted_characters = list(set(characters))
sorted_characters.sort()
print("")
sys.stdout.write(sorted_characters[3])
sys.stdout.write(sorted_characters[2])
sys.stdout.write(sorted_characters[4])
sys.stdout.write(sorted_characters[4])
sys.stdout.write(sorted_characters[5])
sys.stdout.write(sorted_characters[0])
sys.stdout.write(sorted_characters[7])
sys.stdout.write(sorted_characters[5])
sys.stdout.write(sorted_characters[6])
sys.stdout.write(sorted_characters[4])
sys.stdout.write(sorted_characters[1])
