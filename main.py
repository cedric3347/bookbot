import sys
from stats import count_words, count_letters, sorted_count


def get_book_text():
  with open(sys.argv[1]) as f:  # Open the file at filepath
    contents = f.read()                      # Read the file's contents
    return contents                          # Return the contents


def main():
  num_words = count_words(get_book_text())
  num_letters = count_letters(get_book_text())
  sorted_letters = sorted_count(num_letters)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  
  for letter_dict in sorted_letters:
    char = letter_dict["char"]
    count = letter_dict["count"]

    if char.isalpha():  
      print(f"{char}: {count}")
  print("============= END ===============")

if len(sys.argv) !=2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
else:

# Call main at the bottom
  main()
