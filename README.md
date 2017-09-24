OSM Bookmark Collection
=======================
This is a collection of bookmarks for use in Firefox and Chromium at trade fairs (e.g. Intergeo) and other events where OSM is presented to people outside the community (e.g. Linuxtag). This collection aims to contain a lot of important websites and maps of following categories:

* OSM-based maps (apart from simple maps overlaying OSM with own/propietary data)
* software for OSM data
* OSM-based commercial services (including company websites)
* documentation about OSM

This collection is very German-centric and contains only German descriptions.

Contributing
============
You can import the .html file into your Firefox or Chromium profile. Please use a separate browser profile (start Firefox from Shell using `firefox --ProfileManager`).

Entries are managed in a JSON file and the HTML file for import into Firefox and Chromium is generated using a Python script.

Too build the HTML file, just use the Makefile. There are very few dependencies – just Python 3.x, no extra packages.

```sh
make
```


License
=======
Copyright © 2015 Nakaner and others
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
