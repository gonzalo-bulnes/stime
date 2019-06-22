build: clean
	python setup.py sdist bdist_wheel

upload_to_test_pypi:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload_to_pypi:
	python -m twine upload dist/*

clean:
	-rm -r dist/
