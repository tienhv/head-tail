from setuptools import setup

setup(
	name='tail',
	version='1.0',
	py_modules=['tail'],
	entry_points='''
		[console_scripts]
		tail=tail:tail2
		head=tail:head
	''',
)