from stats import get_num_words, character_count, sort_dict
import sys


def get_book_text(book_path: str) -> str:
    with open(book_path, 'r') as f:
        file_contents =  f.read()
    return file_contents


def main():
    if len(sys.argv)!=2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    

    book_path = sys.argv[1] #'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = character_count(book_text)
    char_sorted_list = sort_dict(num_chars)
    print('============ BOOKBOT ============')
    print('Analyzing book found at {file_path}...'.format(file_path=book_path))
    print('----------- Word Count ----------')
    print('Found {num_words} total words'.format(num_words=num_words))
    print('--------- Character Count -------')
    for d in char_sorted_list:
        print('{k}: {v}'.format(k=d.get('char'), v=d.get('num')))
    print('============= END ===============')
if __name__ == '__main__':
    main()
