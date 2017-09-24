#! /usr/bin/env python3

import sys
import json

def write_header():
    header = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Lesezeichen-Menü</H1>

<DL><p>\n"""
    sys.stdout.write(header)

def write_indent(amount):
    for i in range(0, amount):
        sys.stdout.write("  ")

def handle_leaf(leaf, additional_depth=0):
    write_indent(additional_depth)
    try:
        if "tags" in leaf:
            sys.stdout.write("    <DT><A HREF=\"{}\" TAGS=\"{}\">{}</A>\n".format(leaf["url"], leaf["tags"], leaf["name"]))
        else:
            sys.stdout.write("    <DT><A HREF=\"{}\">{}</A>\n".format(leaf["url"], leaf["name"]))
    except KeyError as err:
        print(leaf)
        exit(1)

def handle_group(group, additional_depth):
    write_indent(additional_depth)
    sys.stdout.write("<DT><H3>{}</H3>\n".format(group["name"]))
    write_indent(additional_depth)
    sys.stdout.write("  <DL><p>\n".format(group["name"]))
    for leaf in group["members"]:
        if "url" in leaf:
            handle_leaf(leaf)
        elif "members" in leaf:
            parse_entry(leaf, additional_depth + 1)
        else:
            sys.stderr.write("Following element has neither a member \"key\" nor a member \"url\": {}\n".format(group))
            exit(1)
    sys.stdout.write("  </DL><p>\n")
    

def parse_entry(entry, addition_depth=0):
    if "members" in entry:
        handle_group(entry, addition_depth)
    elif "url" in entry:
        handle_leaf(entry, addition_depth)
    else:
        sys.stderr.write("invalid entry: {}\n".format(json.dumps(entry), indent=2))


def iterate_bookmarks(bookmarks):
    write_header()
    for entry in bookmarks:
        parse_entry(entry)
    sys.stdout.write("</DL>\n")


with open(sys.argv[1], "r") as fp:
    bookmarks = json.load(fp)
    iterate_bookmarks(bookmarks)

