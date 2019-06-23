test:
	@# See https://stackoverflow.com/a/24736236/3767264
	@( \
		. timer_venv/bin/activate; \
		pip install -r requirements.txt > /dev/null; \
		python -m unittest -v; \
		deactivate \
	)
