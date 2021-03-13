.PHONY: init test lint run

init:
	pipenv install --dev

test:
	pipenv run python -m pytest

lint:
	pipenv run pylint gameoflife

reformat:
	pipenv run black gameoflife

run:
	pipenv run python driver.py input.txt

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache

make zip:
	git ls-files | zip -@ gameoflife.zip

