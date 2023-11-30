#!/usr/bin/env python3


class BookIndexer:
    def __init__(self):
        # A dictionary to store the word-to-page mapping
        self.words = {}
        # A set to store the words that should be excluded from indexing
        self.exclude_words = set()

    def load_exclude_words(self, exclude_words_file):
        # Load the exclude words from the specified file and add them to the set
        with open(exclude_words_file, 'r') as file:
            for word in file.read().split():
                self.exclude_words.add(word.lower())

    def index_book(self, book_file1, book_file2, book_file3):
        # Add the page number count 
        page_no = 0
        # Iterate over the specified book files
        
        for book_file in [book_file1, book_file2, book_file3]:
            with open(book_file, 'r', encoding="utf-8") as file:
                text = file.read()
                # Split the text into pages
                pages = text.split('\n\n')
                page_no += 1
                # Iterate over the pages and index the words
                for page in pages:

                    
                    # Find all words in the page 
                    words = page.split()

                    # Iterate over the words and add them to the index if they are not excluded
                    for word in words:
                        # Remove any leading or trailing punctuation from the word
                        word = word.strip('.,;/:?!-()–“•\'"')
                        # Remove any digits
                        if any(char.isdigit() for char in word):
                            continue
                        word_lower = word.lower()
                        if word_lower not in self.exclude_words:
                            if word_lower not in self.words:
                                # Create a new set for the word if it is not already in the index
                                self.words[word_lower] = set()
                            # Add the page number to the set for the word
                            self.words[word_lower].add(page_no)

    def write_index(self, index_file):
        # Write the index to the specified file
        with open(index_file, 'w') as file:
            file.write("Word : Page Numbers\n")
            file.write("-------------------\n")
            self.words.pop('')
            for word in sorted(self.words.keys()):
                # Sort and convert the set of page numbers to a comma-separated string
                pages = sorted(list(self.words[word]))
                page_str = ','.join(str(p) for p in pages)
                file.write(f"{word} : {page_str}\n")

# Create a new BookIndexer object
indexer = BookIndexer()

# Load the exclude words from the specified file
indexer.load_exclude_words('exclude-words.txt')

# Index the specified book files
indexer.index_book('Page1.txt', 'Page2.txt', 'Page3.txt')

# Write the index to the specified file
indexer.write_index('index.txt')
