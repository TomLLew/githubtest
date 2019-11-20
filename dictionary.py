phonebook = {'tim' : '12350564871',
             'jim' : '54895123756',
             'dave' : '85130489541',
             'leigh' : '03245687512',
             'john' : '56712332145'
    }

print(phonebook.keys())
print(phonebook.values())
print(phonebook['tim'])


empty_dict = {}
empty_dict['jim'] = 'jimbob'
empty_dict['bob'] =  'bobjim'
empty_dict['cow'] = 'goes mooooo'

print(empty_dict.keys())


i = 0
a = {}
while i < 3:
    fname = input('first name: ')
    lname = input('last name:  ')
    a.update({fname: lname})
    print(a)
    i += 1



print(a.keys())
print(a.values())
print(a)
