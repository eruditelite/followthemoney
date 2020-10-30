##
Download by selecting "Data Export" and choosing XML.  Copy the link and

wget --wait=2 \
     --level=inf \
      --limit-rate=20K \
      --recursive \
      --page-requisites \
      --user-agent=Mozilla \
      --no-parent \
      --convert-links \
      --adjust-extension \
      --no-clobber \
      -e robots=off \
	  'the link you copied above'

This will create a directory, api.followthemoney.org that contains a
file.  The file will be something like 'index.html?dt=...'.  You
should be able to see the search etc.

##
Clean up the file with the following.

xmllint --format api.followthemoney.org/index... > output.xml

This is now fairly readable, and should be parsable using Python.
