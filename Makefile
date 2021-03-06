all: venv ghgrenamer/mappings.py

venv: dev-requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur dev-requirements.txt
	touch venv

ghgrenamer/mappings.py: names.yaml scripts/create_mappings.py venv
	./venv/bin/python scripts/create_mappings.py

test: venv ghgrenamer/mappings.py
	./venv/bin/pytest tests

publish-on-testpypi: venv
	-rm -rf build dist
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		./venv/bin/python setup.py bdist_wheel --universal; \
		./venv/bin/twine upload -r testpypi dist/*; \
	else \
		echo Working directory is dirty >&2; \
	fi;

test-testpypi-install: venv
	$(eval TEMPVENV := $(shell mktemp -d))
	python3 -m venv $(TEMPVENV)
	$(TEMPVENV)/bin/pip install pip --upgrade
	$(TEMPVENV)/bin/pip install \
		-i https://testpypi.python.org/pypi ghgrenamer \
	# Remove local directory from path to get actual installed version.
	$(TEMPVENV)/bin/python -c "import sys; sys.path.remove(''); import ghgrenamer; print(ghgrenamer.__version__)"

publish-on-pypi: venv
	-rm -rf build dist
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		./venv/bin/python setup.py bdist_wheel --universal; \
		./venv/bin/twine upload dist/*; \
	else \
		echo Working directory is dirty >&2; \
	fi;

test-pypi-install: venv
	$(eval TEMPVENV := $(shell mktemp -d))
	python3 -m venv $(TEMPVENV)
	$(TEMPVENV)/bin/pip install pip --upgrade
	$(TEMPVENV)/bin/pip install ghgrenamer
	$(TEMPVENV)/bin/python -c "import sys; sys.path.remove(''); import ghgrenamer; print(ghgrenamer.__version__)"

flake8: venv
	./venv/bin/flake8 pymagicc

.PHONY: publish-on-testpypi test-testpypi-install publish-on-pypi test-pypi-install flake8
