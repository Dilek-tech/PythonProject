string1 = "Greetings, Earthlings"
print(string1[0])  # Prints “G”
print(string1[4:8])  # Prints “ting”
print(string1[11:])  # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

print(string1[-10:])  # Prints “Earthlings” again

print(string1[55:])  # Prints “”
print(string1[0::2])  # Prints “Getns atlns”
print(string1[::-1])  # Prints “sgnilhtraE ,sgniteerG”

greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!"

phonenum = '2025551212'    # The first 3 digits are the area code:
area_code = "(" + phonenum[:3] + ")"  # print (202)
exchange = phonenum[3:6]  # The next 3 digits are called the “exchange”:
line = phonenum[-4:]  # The last 4 digits are the line number:
print (area_code + " " + exchange + "-" + line)

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
print(format_phone('2025551212'))
