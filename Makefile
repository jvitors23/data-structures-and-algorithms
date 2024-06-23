test:
	pytest .

lint:
	black . && flake8 .