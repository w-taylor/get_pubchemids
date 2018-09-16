# get_pubchemids

Takes as an input a csv file with no header and one compound name per line.
The site www.ncbi.nlm.nih.gov/pccompound is queried with each drug name and the PubChem ID of top result is taken.
The output is a csv file with a column for drugnames and a column for associated PubChem IDs. If no PubChem ID was found, the PubChem ID column is left blank for that row.



## Required Libraries

* requests
* csv
* BeautifulSoup

## To do list:

* Eliminate empty row added between every entry in output file
* Some compounds when queried lead directly to a drug page rather than the usual search result page, this leads to the incorrect info being scraped from the page. These entries always have a decimal in the output file PubChem ID so they are easy to spot
* Dashes are replaced by underscores and spaces are replaced with + when querying, but these sanitized drugnames are used for the output file as well. Would be better if the original names were used in the output file
