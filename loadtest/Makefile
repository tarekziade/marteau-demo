.PHONY: build test bench

# build virtualenv
build:
	virtualenv --no-site-packages .
	bin/pip install funkload

# run a single test, for sanity-checking
test:
	bin/fl-run-test stress.py

# run bench
bench:
	bin/fl-run-bench stress.py StressTest.test_simple

