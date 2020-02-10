SUBDIR+= 	cli
SUBDIR+= 	docs
SUBDIR+= 	libheaper

SUBDIR_GOALS?= 	all clean distclean


.PHONY: depends
depends:
	pip3 install -r requirements.txt

.PHONY:  install
install: depends
	pip3 install .

.PHONY: environment
environment:
	pipenv install -e .

requirements.txt:
	pigar -c



INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
