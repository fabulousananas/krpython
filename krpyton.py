text = "... «наивный» - <есть> натуральный, природный, не обработанный искусственными условностями цивилизации. Так что если наша культура есть продолжение природы, её язык (по распространенному мнению философов), её заявление о себе, то в наивном человеке и его слове - это прямейше, спонтанно, без опосредованных звеньев...  — Георгий Гачев, «Плюсы и минусы наивного философствования»"

def clean_text(text, trash_tokens):

    #Очистка всех символов
    text = text.strip(trash_tokens)
    return text


def get_words(text):

    trash_tokens = "!@#$%^&*()_{}[]-+«»<>?.,/\|"
    tokens = text.split()
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_tokens)
        if clean_token != "":
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens

print(get_words(text))

def main():

    filename = "C:\\Users\\student\\Desktop\\quotes.txt"
    DASH = "—"
    
    with open (filename, encoding = "utf-8") as fid:
        for line in fid:
            parts = line.split(DASH)
            quote = parts[0]
            author = parts[1]

            quote_words = get_words(quote)

            if len(quote_words) < 10:
                print(quote)

if __name__ = "__main__"
    main()

