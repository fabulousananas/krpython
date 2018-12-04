text = '... «наивный» - <есть> натуральный, природный, не обработанный искусственными условностями цивилизации. Так что если наша культура есть продолжение природы, её язык (по распространенному '

def clear_text(text, trash_tokens):
    #Очистика левой части
    #while len(text) > 0 and text[0] in trash_tokens:
    #   text = text[:1]
    text = text.strip(trash_tokens)
    return text

def get_words(text):
    trash_tokens = '.,/?!@#$%^&*(){}[]_\|<>:;—'
    tokens = text.split()
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_tokens)
        if clean_token != '':
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens

def find_quotes(input_word, all_quotes, all_quotes_words):
    result = []
    for i, quote in enumerate(all_quotes):
        if input_word in all_quotes_words[i]:
            result.append(quote)
    return result
       
def main():
    filename = 'quotes.txt'
    DASH = '—'
    all_quotes = []
    all_quotes_words = []
    
    with open(filename, encoding='utf-8') as fid:
        for line in fid:
            parts = line.split(DASH)
            quote = parts[0].strip()
            quote_words = get_words(quote)

            all_quotes.append(quote)
            all_quotes_words.append(quote_words)

    while True:
        input_word = input('Введите слово: ')
        if input_word == '':
            break
        input_word = input_word.strip().lower()
        found = find_quotes(input_word, all_quotes, all_quotes_words)
        if len(found) == 0:
            print('Ничего не найдено')
        else:
            for quote in found:
                print(quote)
        
if __name__ == '__main__':
    main()
