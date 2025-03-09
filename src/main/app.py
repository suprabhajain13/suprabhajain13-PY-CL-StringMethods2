from lab import (
    replace_characters,
    split_string,
    join_strings,
    count_occurrences,
    find_char_index,
    starts_with_substring,
    ends_with_substring
)

if __name__ == "__main__":
    my_string = "Hello, Python!"
    print("Original string:", my_string)
    
    # Replacing characters in a string
    replaced_string = replace_characters(my_string, "Python", "World")
    print("Replaced string:", replaced_string)
    
    # Splitting a string
    splitted_string = split_string(my_string, " ")
    print("Splitted string:", splitted_string)
    
    # Joining a list of strings
    my_list = ["Hello", "Python", "World"]
    joined_string = join_strings(my_list, " ")
    print("Joined string:", joined_string)
    
    # Counting the occurrences of a character in a string
    count = count_occurrences(my_string, "l")
    print("Number of occurrences of 'l':", count)
    
    # Finding the index of a character in a string
    index = find_char_index(my_string, "P")
    print("Index of character 'P':", index)
    
    # Checking if a string starts with a specific substring
    starts_with = starts_with_substring(my_string, "Hello")
    print("Does the string start with 'Hello'? :", starts_with)
    
    # Checking if a string ends with a specific substring
    ends_with = ends_with_substring(my_string, "Python!")
    print("Does the string end with 'Python!'? :", ends_with)
