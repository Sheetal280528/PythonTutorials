#Dictionary is also one built-in data type in python but it can be like below
# Dict is not ordered (list, string, tuple all these have index which makes it ordered; we know what comes at which place)
# Dict is mutable/changeable (list is mutable but tuple & string not)
# Dict no duplicates allowed (list, tuple, str allows duplicate) which means key field should be unique
info_dict = {
     "name"                    : "sheetal",
     "age"                     : 36,
     "marks"                   : 95.5,
     "subject"                 : ["maths", "english", "evs"],
     12                        : 87.50,
     45.5                      : "english marks",
     ("college", "university") : ("lnct", "rgpv")
}
print(info_dict)
#{'name': 'sheetal', 'age': 36, 'marks': 95.5, 'subject': ['maths', 'english', 'evs'], '12': 87.5, '45.5': 'english marks', ('college', 'university'): ('lnct', 'rgpv')}
print(type(info_dict))    #<class 'dict'>

#elements can be accessed by key fields (no index is in dict so can not be used via index)
print(info_dict["name"])    #sheetal
print(info_dict["college","university"])  # ('lnct', 'rgpv')
print(info_dict[12])        #87.5

#elements can be updated using key fields and new key fields can also be added to the dict
info_dict["name"] = "Ayansh"
print(info_dict)
{'name': 'Ayansh', 'age': 36, 'marks': 95.5, 'subject': ['maths', 'english', 'evs'], 12: 87.5, 45.5: 'english marks', ('college', 'university'): ('lnct', 'rgpv')}
info_dict["surname"] = 'Rai'
print(info_dict)
#{'name': 'Ayansh', 'age': 36, 'marks': 95.5, 'subject': ['maths', 'english', 'evs'], 12: 87.5, 45.5: 'english marks', ('college', 'university'): ('lnct', 'rgpv'), 'surname': 'Rai'}

null_dict = {}
print(null_dict)   #{}
null_dict["name"] = "Test23"
print(null_dict)   #{'name': 'Test23'}

#nested dictionary
student_dict = {
             "name" : ["sheetal", 25, "Ayansh"],
             "subject" : { "subname" : ("math", "physics"),
                           "marks"   : (89.89, 76)
                         },
            "school" : "lnct"   
             }
print(student_dict)
#{'name': ['sheetal', 25, 'Ayansh'], 'subject': {'subname': ('math', 'physics'), 'marks': (89.89, 76)}, 'school': 'lnct'}

print(student_dict["name"])
#['sheetal', 25, 'Ayansh']

print(student_dict["subject"])
#{'subname': ('math', 'physics'), 'marks': (89.89, 76)}

print(student_dict["subject"]["marks"])
#(89.89, 76)

print(len(student_dict))    #3 -- it has 3 key fields that is its length

#print all the key fields
print(student_dict.keys())  #dict_keys(['name', 'subject', 'school'])

#print all the value fields
print(student_dict.values())
#dict_values([['sheetal', 25, 'Ayansh'], {'subname': ('math', 'physics'), 'marks': (89.89, 76)}, 'lnct'])

#type casting, keys or values can be type casted into lists or tuples
print(list(student_dict.keys()))  #['name', 'subject', 'school']
print(tuple(student_dict.keys())) #('name', 'subject', 'school')

print(list(student_dict.values()))
#[['sheetal', 25, 'Ayansh'], {'subname': ('math', 'physics'), 'marks': (89.89, 76)}, 'lnct']

print(tuple(student_dict.values()))
#(['sheetal', 25, 'Ayansh'], {'subname': ('math', 'physics'), 'marks': (89.89, 76)}, 'lnct')

print(student_dict.items())
#dict_items([('name', ['sheetal', 25, 'Ayansh']), ('subject', {'subname': ('math', 'physics'), 'marks': (89.89, 76)}), ('school', 'lnct')])     

student_dict["age"] = [24, 78, 87]
print(student_dict)
#{'name': ['sheetal', 25, 'Ayansh'], 'subject': {'subname': ('math', 'physics'), 'marks': (89.89, 76)}, 'school': 'lnct', 'age': [24, 78, 87]}  
student_dict["name"] = "Sheetal"
print(student_dict)
{'name': 'Sheetal', 'subject': {'subname': ('math', 'physics'), 'marks': (89.89, 76)}, 'school': 'lnct', 'age': [24, 78, 87]}


print(student_dict.keys()) #dict_keys(['name', 'subject', 'school', 'age'])
print(student_dict["name"])      ## if the passsed key is not avaiable then it returns error
print(student_dict.get("name"))  ## if the passed key is not available then this returns None
print("student_dict: ", student_dict)
### In this example, when an item is deleted from the dictionary, the change is reflected in the view object returned by items().
items = student_dict.items()
print("items: ", student_dict.items())
#items:  dict_items([('name', 'Sheetal'), ('subject', {'subname': ('math', 'physics'), 'marks': (89.89, 76)}), ('school', 'lnct'), ('age', [24, 78, 87])])
del student_dict["subject"]
print("updated items: ", student_dict.items())
#updated items:  dict_items([('name', 'Sheetal'), ('school', 'lnct'), ('age', [24, 78, 87])])

### update method
student_dict.update({"test" : "testupdate"})
print(student_dict)
new_dict = {"subject" : ("maths", "english")}
student_dict.update(new_dict)
print(student_dict)
