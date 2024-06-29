
calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    len_ = (len(string))
    up = string.upper()
    lo = string.lower()
    return (len_, up, lo)

def is_contains(string, list_to_search):
    count_calls()

    for i in list_to_search:
        if isinstance(i, str):
            if i.lower() == string.lower():
                return True
    return False

print(string_info('Zarigueya'))

print(string_info('extraVagante'))

print(string_info("железныЙ"))

print(is_contains('pEro', [2, 'pErO', 'no', 'como']))
print (is_contains('Zarigueya', ['я', 'ты', 'он']))

print(calls)




