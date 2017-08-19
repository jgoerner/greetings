# Testing the code
test:
	python -m pytest -v tests/

# Calculating coverage, CLI report
coverage:
	python -m pytest --cov

# Calculating coverage, HTML report
coverage_html:
	python -m pytest --cov --cov-report html:cov_html
