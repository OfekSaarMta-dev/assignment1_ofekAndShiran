import json
import pickle

def load_lexicon(filename):
    """Loads the lexicon as a set of words from a file."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return None
    with open(filename, 'rb', encoding='utf8') as file:
        return set(word.strip() for word in file.readlines())


def decipher_phrase(phrase, lexicon_filename, abc_filename):
    # todo: implement this function
    print(f'starting deciphering using {lexicon_filename} and {abc_filename}')

    result = {"status": 1, "orig_phrase": '', "K": -1} # if we cant decipher what should we return !!!!!!!!
    return result



# todo: fill in your student ids
students = {'id1': '322756586', 'id2': '211449145'}

if __name__ == '__main__':
    with open('config-decipher.json', 'r') as json_file:
        config = json.load(json_file)

    # note that lexicon.pkl is a serialized list of 10,000 most common English words
    result = decipher_phrase(config['secret_phrase'],
                             config['lexicon_filename'],
                             config['abc_filename'])

    assert result["status"] in {1, -1, 0}

    if result["status"] == 1:
        print(f'deciphered phrase: {result["orig_phrase"]}, K: {result["K"]}')
    elif result["status"] == -1:
        print("cannot decipher the phrase!")
    else:  # result["status"] == 0:
        print("empty phrase")
