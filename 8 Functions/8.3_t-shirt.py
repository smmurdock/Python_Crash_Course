def make_shirt(size, text):
	"""Accepts a size and the text of a message that should be printed on the shirt"""
	print(f'You have ordered a shirt with the print: \"{text}\" in size {size.title()}.')

make_shirt('small', 'Stay Kind')
make_shirt(text='Oyster City Brewing Company', size="medium")