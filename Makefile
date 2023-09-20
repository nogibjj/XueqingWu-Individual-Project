install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --nbval --cov=main --cov=mylib test_*.py *.ipynb

format:	
	black *.py 

lint:
	ruff check *.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy

# Auto generate graph and summary
generate_and_push:
 # Create the markdown file (assuming it's generated from the plot)
	python main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add Rating_plot.png MetaScore_plot.png imdb_movie_summary.md; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

