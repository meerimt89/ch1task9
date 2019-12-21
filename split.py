pizza = [
    'first item', 'second item', 'third item', 'fourth item', 'fifth item', seventh item', 'eights item
]
for item in pizza:
    print (f'eating {item} of pizza')
    print(item.split('_')[0])
new_list = []
    for item in pizza:
        new_list.append(item.split('_')[0])
print(new_list)

enumerations = []
for index, item in enumerate(pizza):
    print(f'This is index {index}', and item ---{item}')
    new_item = item.split('_')[0]
    enumerations.append(new_item.title())
print(enumerations)


