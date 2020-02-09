.PHONY: all
all: heaper.pdf


# Documentation

heaper.pdf: heaper.tex abstract.tex ../LICENSE heaper.bib


# Includes

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk

