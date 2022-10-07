install: # Install dependency
	poetry install

brain-games: # Start application
	poetry run brain-games

build: # Building an application
	poetry build

publish: # Package publication
	poetry publish --dry-run

package-install: # Installing the package for the current user
	python3 -m pip install --user dist/*.whl

lint: # Start linter
	poetry run flake8 brain_games

brain-even: # Start games
	poetry run brain-even

package-install-f: # Force installing the package for the current user
	python3 -m pip install --user --force-reinstall dist/*.whl