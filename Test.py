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