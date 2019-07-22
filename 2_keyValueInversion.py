d = {'key1': 'value1', 'key2': 'value2'}
for i in d.keys():
	d[d.pop(i)] = i
print(d.items())
