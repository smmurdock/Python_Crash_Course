def describe_city(city, country='Germany'):
	"""write a sentence about what country the city is in"""
	print(f'{city.title()} is in {country.title()}.')

describe_city('Berlin')
describe_city('munich')
describe_city('Reykjavik', 'iceland')