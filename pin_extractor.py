"""
Daily Python Project: Poem PIN Extractor
Author: Your Name
Description: An algorithmic puzzle that extracts a secret numeric PIN from 
             a list of poems by analyzing diagonal word lengths across lines.
"""

def pin_extractor(poems: list[str]) -> list[str]:
    """
    Extracts a secret numeric code from a collection of poems.
    
    The algorithm inspects each line of a poem sequentially. From each line, 
    it grabs the word located at the current line's index position and notes 
    its length. If the line is too short to have a word at that index, a '0' 
    is added instead.
    
    Args:
        poems (list): A list of strings, where each string represents a multi-line poem.
        
    Returns:
        list: A list of stringified numeric secret codes (PINs).
    """
    secret_codes = []
    
    for poem in poems:
        secret_code = ''
        # Split the multi-line string into individual lines
        lines = poem.split('\n')
        
        for line_index, line in enumerate(lines):
            # Split the current line into a list of words
            words = line.split()
            
            # Check if there are enough words to access the diagonal index
            if len(words) > line_index:
                # Target the word matching the current line number
                target_word = words[line_index]
                # Append the length of that specific word to the code string
                secret_code += str(len(target_word))
            else:
                # Fallback to '0' if the line doesn't contain enough words
                secret_code += '0'
                
        secret_codes.append(secret_code)
        
    return secret_codes


if __name__ == "__main__":
    # Test Data Structures
    poem1 = """Stars and the moon
shine in the sky
white and
until the end of the night"""

    poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
    poem3 = "There\nonce\nwas\na\ndragon"

    # Execution and Console Output
    print("--- Executing Pin Extractor Algorithm ---")
    results = pin_extractor([poem1, poem2, poem3])
    print(f"Extracted Secret Codes: {results}")
