"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """
    new_words = [vocab_words[0]]
    for word in vocab_words[1:]:
        print(word)
        new_words.append(vocab_words[0]+word)
        print(new_words)
        
    return ' :: '.join(new_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """
    
tests = ['heaviness', 'sadness']
def remove_suffix_ness(word):

    without_ness = word[0:-4]
#    print(without_ness)
    if without_ness[-1] == 'i':
#            print(without_ness[0:-1] + 'y')
            return without_ness[0:-1] + 'y'
    else:
 #           print(without_ness)
            return without_ness
        
for test in tests:
    remove_suffix_ness(test)


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """

    removed_period = sentence[0:-1]
    words = removed_period.split(' ')
    verb = words[index] + 'en'
    return verb
