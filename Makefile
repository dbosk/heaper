.PHONY: all
all: heapq.pdf heapq

SRC+=	heapq.nw
SRC+=	building.mk.nw

.PHONY: clean
clean:
	${RM} ${OBJ}

# Documentation

heapq.pdf: heapq.nw abstract.tex LICENSE heapq.bib
heapq.pdf: building.tex

OBJ+=	heapq.pdf

building.tex: building.mk.nw

OBJ+=	building.tex


# Program

heapq.py: ${SRC}

OBJ+=	heapq.py

heapq: heapq.py
	${CP} $^ $@

OBJ+=	heapq

pushq popq peekq: heapq
	ln -s $^ $@

OBJ+=	pushq popq peekq


# Package

PKG_NAME-main= 			heapq
PKG_FILES-main= 		heapq
PKG_PREFIX-main= 		/usr/local
PKG_DIR-main= 			/bin
PKG_TARBALL_FILES-main= ${PKG_FILES-main} Makefile


# Includes

heapq.mk: ${SRC}
include heapq.mk

OBJ+=	heapq.mk

INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
include ${INCLUDE_MAKEFILES}/package.mk

