# задание1
def all_divisors(number):
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# задание2
def three_args(*, var1=None, var2=None, var3=None):
    arguments=[]
    if var1 is not None:
        arguments.append(f'var1={var1}')
    if var2 is not None:
        arguments.append(f'var2={var2}')
    if var3 is not None:
        arguments.append(f'var3={var3}')

    if arguments:
        print('переданы аргументы: ',', '.join(arguments))
    return arguments


# задание3
def palindrom(pal):
    if len(pal)<=1:
        return 'да, это палиндром'
    if pal[0]!=pal[-1]:
        return 'это не палиндром'
    return palindrom(pal[1:-1])


#задание 4
def text_reader(text):
    #разбираем текст на слова
    words=text.split()

    word_count={}
    max_words=''
    long_word='' #переменные для хранения длинного и частых слов

    for word in words:
        #удаляет знаки препинания
        word.strip('.?/!@#$%^*&][{},:;()')
        if word:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1

            if len(word)>len(long_word):     #проверка на длинну
                long_word=word

            if word_count[word]>word_count.get(max_words, 0):  #проверка на частоту
                max_words=word
    print('часто встречаемое слово в тексте: ', max_words,'  самое длинное слово: ', long_word)


#задание 5


# задание 6



#сложнаааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа