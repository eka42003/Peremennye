
calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    n = (len(string))
    m = string.upper()
    od = string.lower()
    print(n, m, od)

def is_contains(string, list_to_search):
    count_calls()
    compar = False

    for i in list_to_search:
        if i.lower() == string.lower():
            compar = True
        else:
           continue
    print(compar)

string_info('Zarigueya')

string_info('extraVagante')

string_info("железныЙ")

is_contains('pEro', ['f', 'pErO', 'no', 'como'])
is_contains('Zarigueya', ['я', 'ты', 'он'])

print(calls)




