from stats import num_Words, get_book_text, letter_count, sorted_list, final_sort
import sys

def main():
    # Check if we have the right number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # If we get here, we have the right number of arguments
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------") 
    num_Words(get_book_text(book_path))
    print("--------- Character Count -------")
    sorted_list(letter_count(get_book_text(book_path)))
    final_sort(sorted_list(letter_count(get_book_text(book_path))))
    
    # We only exit with status code 1 if there's an error
    # For successful execution, either don't call sys.exit() or use sys.exit(0)

main()