#Makefile

full-test:
	poetry run pytest --show-capture=stdout --disable-pytest-warnings -v --tb=no
light-test:
	poetry run pytest -vv
lint:
	poetry run flake8 .
check: light-test lint
push: check
	git push


install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
