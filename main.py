def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    print("---   Begin Report   ---")
    print()
    print("Word Count: " , word_counter(file_contents))
    # print()
    # print("Unique char: ",  unique_char_counter(file_contents))
    print()
    print_char_count(unique_char_counter(file_contents))
    print()
    print("---   End Report   ---")

def word_counter(string):
    return len(string.split())

def unique_char_counter(string):
    lower = string.lower()
    char_counted = {}
    for char in lower:
        if char in char_counted:
            char_counted[char] += 1
        else:
            char_counted[char] = 1
    return char_counted


def print_char_count(char_dic):
    for key in char_dic:
        if key.isalpha():
            print(f"The '{key}' character was found {char_dic[key]} times")



main()
