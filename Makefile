test:
	python -m pytest -v tests/

coverage:
	python -m pytest --cov

coverage_html:
	python -m pytest --cov --cov-report html:cov_html
