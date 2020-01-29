from hash import HashTable

def test_add():
	table = HashTable()
	assert('qwe' not in table)
	table.add('qwe')
	assert('qwe' in table)

def test_remove():
	table = HashTable()
	table.add('qwe')
	assert('qwe' in table)
	table.remove('qwe')
	assert('qwe' not in table)

def test_repr():
	table = HashTable()
	assert(table)
	table.add('qwe')