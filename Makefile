build: clean
	python setup.py sdist bdist_wheel

upload_to_test_pypi:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload_to_pypi:
	python -m twine upload dist/*

clean:
	-rm -r dist/

test_stime:
	@# See https://stackoverflow.com/a/24736236/3767264
	@( \
		. venv/bin/activate; \
		python -m unittest -v; \
		deactivate \
	)

test_example_timer:
	@$(MAKE) --no-print-directory -C examples/timer test

test: test_stime test_example_timer
