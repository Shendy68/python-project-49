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

brain-even: # Start games even numbers
	poetry run brain-even

package-install-f: # Force installing the package for the current user
	python3 -m pip install --user --force-reinstall dist/*.whl

brain-calc: # Start games calc
	poetry run brain-calc

brain-gcd: # Start games gcd numbers
	poetry run brain-gcd

brain-progression: # Start games numbers progression
	poetry run brain-progression

brain-prime: # Start games prime numbers
	poetry run brain-prime