""" Reads a file input by the user and analyses the paragraphs, finds all the unique words,
    prints out each unique word and in which paragraphs that word is and finds out how many the word
    occured totally in all paragraphs together. """


import string
import operator


def get_file_name():
    """Gets name of the file from the user."""
    filename = input("Enter filename: \n")
    
    return filename


def open_file(filename):
    """Tries to open the file, if the file does not exist, prints an error message."""
    try:
        file_object = open(filename, "r+")
        return file_object
    except FileNotFoundError:  # If the file isn't found, prints out an error.
        print("Filename {} not found!".format(filename))        
        return None


def make_list(file_object):
    """Reads file object and creates a list with sublists for each paragraph."""
    temp_list = []
    main_list = []
    counter = 0    
    for line in file_object:
        line_list = []
        line_list = line.split()
        if not line_list:  # Checks if the current line has any words in it.
            counter += 1
            main_list.append(temp_list)
            temp_list = [] 
        for word in line_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            temp_list.append(word)     
    main_list.append(temp_list)

    return main_list


def get_all_words(main_list):
    """Adds all unique words to a list and sorts it."""
    all_words = []
    for sublist in main_list:
        for word in sublist:
            if word not in all_words:
                all_words.append(word) 

    return sorted(all_words)


def paragraph_index(all_words, main_list):
    """Finds in which paragraph/s a word in mentioned.

    Iterates through the sublists in the main_list and finds in which sublist(paragraph)
    that word is used, returns the results as a dictionary.
    """
    my_dict = {}
    for word in all_words:
        temp_list = []
        for sublist in range(len(main_list)):
            if (word in main_list[sublist]) and (word not in temp_list):  # Makes sure that the same word isn't checked twice.
                temp_list.append(sublist + 1)
        temp_tuple = tuple(temp_list)        
        my_dict[word] = temp_tuple
        
    return my_dict


def word_counter(main_list):
    """Create a dictionary of words and times used.

    Iterates through the sublists in main_list and checks every word in the sublists,
    returns a dictionary with every word used and how many times it was used. 
    """
    count_dict = {}
    for sublist in main_list:
        for word in sublist:
            if word not in count_dict:  # Adds the word to the dictonary if it's not already there.
                count_dict[word] = 1
            else:  # Increases the value of the word if the word is already in the list.
                count_dict[word] += 1
                
    return count_dict


def word_index_print(my_dict):
    """Prints out the words and in which paragraphs they are."""
    print("The paragraph index: ")
    for key,val in my_dict.items():
        counter = 0
        print("{}".format(key), end=" ")
        for i in val:
            if counter != 0:
                print(end=", ")
                print(i, end="")
            else:
                print(i, end="")
                counter += 1
        print() 


def top_words(count_dict):
    """This function returns a sorted list of the words with their counter."""
    count_dict_2 = sorted(count_dict.items())  # Creates a list from the dict and sorts it alphabetically.
    sorted_count = sorted(count_dict_2 ,key=operator.itemgetter(1), reverse=True)  # Sorts the top numbers as descending.

    return sorted_count


def top_list_maker(sorted_count, length):
    """Returns a list of the most common words for the givent length of the list."""
    top_list = []
    for i in range(0, length):
        top_list.append(sorted_count[i])
        
    return top_list


def top_printer(top_list):
    """Prints out the top list for X words."""
    print("The highest {} counts: ".format(len(top_list)))
    for index in top_list:
        print("{}: {}".format(index[0], index[1]))
    if len(top_list) == 10:
        print()  # Prints an empty line after the top list is done


def main():
    main_list = make_list(file_object)
    all_words = get_all_words(main_list)
    my_dict = paragraph_index(all_words, main_list)
    word_index_print(my_dict)
    count_dict = word_counter(main_list)
    sorted_count= top_words(count_dict)
    top_ten = top_list_maker(sorted_count, 10)
    top_twenty = top_list_maker(sorted_count, 20)
    top_printer(top_ten)
    top_printer(top_twenty)


# Main program starts here.
filename = get_file_name()
file_object = open_file(filename)
if file_object != None:  # If the open_file function returns None, the program stops.
    main()