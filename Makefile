all: bookmarks.html

bookmarks.html:
	python3 json2html.py entries.json > bookmarks.html

clean:
	rm bookmarks.html

