SUBDIR+= 	cli
SUBDIR+= 	docs
SUBDIR+= 	libheaper

SUBDIR_GOALS?= 	all clean distclean


.PHONY: depends
depends:
	poetry install

.PHONY:  install
install: depends
	poetry install

.PHONY: environment
environment:
	poetry install

requirements.txt:
	@echo "Note: Use 'poetry export -f requirements.txt --output requirements.txt --without-hashes' to generate requirements.txt"
	@echo "This requires: poetry self add poetry-plugin-export"



INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
