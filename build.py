#! /usr/bin/env python

import os

DOC_TYPE_MAP = {
    "report": create_report,
    "paper": create_paper
}

# -- INPUTS -- #

# Get target location
location = check_non_empty(raw_input("Choose the location where the new project will be created:\n"), "Location")

# Get document type
doc_type = raw_input("Choose the document type [REPORT/paper]:\n").lower() or "report"

# Only reports can have a separate title page
if doc_type == "report":
    # Ask title page
    has_title = False if (raw_input("Would you like to have a separate title page [y/N]?\n").lower() or "n") == "n" else True

    if has_title:
        # Get title type
        title_type = raw_input("Choose the title page type [REGULAR/image]:\n").lower() or "regular"

        # Ask index
        has_index = False if (raw_input("Would you like to have an index [y/N])?\n").lower() or "n") == "n" else True

        # Ask table of figures
        has_tof = False if (raw_input("Would you like to have a table of figures [y/N]?\n").lower() or "n") else True

# Get title
title = check_non_empty(raw_input("Write the title of your document:\n"), "Title")

# Get authors
authors = check_non_empty(raw_input("Write the author(s) of the document (if more than one please separate by commas):\n"), "Authors")


# -- DOCS GENERATION -- #

project_dir = os.mkdir(location + "/" + title) # Change to makedirs if creation of intermediate level directories is needed
if has_title:
    create_title(title_type, title, authors)

create_doc(doc_type, has_index, has_tof, has_title, title, authors)

def create_doc(doc_type, has_index, has_tof, has_title, title, authors):
    if has_title:
        DOC_TYPE_MAP[doc_type](has_index=has_index, has_tof=has_tof)
    else:
        DOC_TYPE_MAP[doc_type](title=title, authors=authors)

def create_report(title=None, authors=None, has_index=None, has_tof=None):
    # TODO

def create_paper(title=None, authors=None, has_index=None, has_tof=None):
    # TODO

def check_non_empty(input, name):
    if input == "":
        raise name + " must have a value"
