install: # Install dependency
	poetry install

brain-games: # Start application
	poetry run brain-games

build: # Building an application
	poetry build

publish: # Package publication
	poetry publish --dry-run

packkage-install: # Installing the package for the current user
	python3 -m pip install --user dist/*.whl

