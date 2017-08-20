# Testing the code
test:
	python3 -m pytest -v tests/

# Calculating coverage, CLI report
coverage:
	python3 -m pytest --cov=./

# Calculating coverage, HTML report
coverage_html:
	python3 -m pytest --cov=./ --cov-report html:cov_html

# Converting malformed code to comply with PEP8
pep8:
	python3 -m autopep8 --in-place --aggressive --aggressive --recursive .
