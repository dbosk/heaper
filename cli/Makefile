.PHONY: all
all: heaper.pdf heaper


# Documentation

heaper.pdf: heaper.tex abstract.tex LICENSE heaper.bib
heaper.pdf: build.tex
heaper.pdf: libheaper.tex
heaper.pdf: heapercli.tex


# Package

PKG_NAME-main= 			heaper
PKG_PREFIX-main= 		/usr/local
PKG_DIR-main= 			/bin
PKG_INSTALL_FILES-main= heaper
PKG_TARBALL_FILES-main= ${PKG_INSTALL_FILES-main} Makefile


# Cleaning

.PHONY: clean
clean:
	${RM} build.tex libheaper.tex heapercli.tex


# Includes

include build.mk

INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
include ${INCLUDE_MAKEFILES}/pkg.mk

