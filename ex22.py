text = '... «наивный» - <есть> натуральный, природный, не обработанный искусственными условностями цивилизации. Так что если наша культура есть продолжение природы, её язык (по распространенному '

def clear_text(text, trash_tokens):
    #Очистика левой части
    #while len(text) > 0 and text[0] in trash_tokens:
    #   text = text[:1]
    text = text.strip(trash_tokens)
    return text

def get_words(text):
    trash_tokens = '.,/?!@#$%^&*(){}[]-_\|<>:;—'
    tokens = text.split()
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_tokens)
        if clean_token != '':
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens
       
def main():
    filename = 'quotes.txt'
    DASH = '—'
    list_of_authors = []
    with open(filename, encoding='utf-8') as fid:
        for line in fid:
            parts = line.split(DASH)
            quote = parts[0].strip()
            author = parts[1].strip()
            quote_words = get_words(quote)
            if 'разум' in quote_words:
                list_of_authors.append(author)
    print(
        'Слово "разум" содержится в ',
        len(list_of_authors),
        'цитате(ах)')
    print(', '.join(list_of_authors))
                


if __name__ == '__main__':
    main()
