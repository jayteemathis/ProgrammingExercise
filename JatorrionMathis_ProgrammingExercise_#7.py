import re  #import the regular expressions module

def split_into_sentences(paragraph):
    """
    Splits the paragraph into individual sentences.
    Handles sentences that begin with numbers too.
    """
    #this regex splits at '.', '?', or '!' followed by a space or end of line.
    sentence_pattern = r'(?<=[.!?]) +'
    sentences = re.split(sentence_pattern, paragraph)
    return sentences

def display_sentences(sentences):
    """
    Displays each sentence on its own line and shows the count.
    """
    print("\n--- Individual Sentences ---")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence.strip()}")

    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    #prompt the user to enter a paragraph
    paragraph = input("Enter a paragraph: ")

    #splt the paragraph into sentences
    sentences = split_into_sentences(paragraph)

    #show each sentence and the total count
    display_sentences(sentences)

if __name__ == "__main__":
    main()