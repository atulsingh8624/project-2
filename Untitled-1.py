def count_words(sentence):
    """
    Function to count the number of words in a sentence.
    
    Parameters:
        sentence (str): The input sentence or paragraph.
    
    Returns:
        int: The count of words in the sentence.
    """
    # Split the sentence by whitespace to get individual words
    words = sentence.split()
    
    # Return the length of the list of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")

    # Check if the input is empty
    if not user_input:
        print("Error: Input is empty. Please enter a valid sentence or paragraph.")
        return

    # Call the count_words function to count the words in the input
    word_count = count_words(user_input)
    
    # Print the word count to the console
    print("Word count:", word_count)

# Entry point of the script
if __name__ == "__main__":
    main()
