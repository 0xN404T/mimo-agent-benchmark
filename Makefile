install:
	pip install -r requirements.txt

check:
	python -m py_compile benchmark.py

run:
	python benchmark.py
