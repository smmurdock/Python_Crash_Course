def make_shirt(text, size='Large'):
	"""Accepts a size and the text of a message that should be printed on the shirt"""
	print(f'You have ordered a shirt with the print: \"{text}\" in size {size.title()}.')

make_shirt('I love Python')
make_shirt('I love Python', 'medium')
make_shirt('Oyster City Brewing Company', 'small')