def count_words(text):
    words = text.split()                      # Splits the words into a list at the spaces
    return len(words)                         # returns the length of the list


def count_letters(text):
    count_result = {}                         # dict to collect letter                        
    lower_text = text.lower()                 # make all letter lowercase so there are no dup letters  
    for letter in lower_text:                 # loop through all letters and update dict with count
        if letter not in count_result:
            count_result[letter] = 1
      
        else:
            count_result[letter] += 1
    return(count_result)


def sorted_count(char_count):                                           
    chars_list = []                          # Create a list of dictionaries with "char" and "count" keys
    
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
                                               
    def sort_on(dict):                       # Sort the list based on the count values           
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
    