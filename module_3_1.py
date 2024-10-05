
calls = 0
def count_calls():
    global calls
    calls += 1




def string_info(string_1):
    count_calls()
    l = (len(string_1), string_1.upper(), string_1.lower())
    return l




def is_contains(string_2, list_1):
    count_calls()
    string_2 = string_2.upper()
    list_2 = []
    for i in list_1:
        list_2.append(i.upper())    
    return bool(list_2.count(string_2))




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)