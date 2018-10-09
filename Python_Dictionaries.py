#define a dictionary data structure

#dictionaries have keys: values for the element
example_dict = { "class" : "Astro 119",
                "prof"   : "Brant",
                "Awesomeness" : 100 
}

print(type(example_dict))   #will say dict

#get a value via key
course = example_dict["class"]
print(course)

#change a value via key
example_dict["Awesomeness"] += 10      #increase aswesomeness

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
    print(x,example_dict[x])