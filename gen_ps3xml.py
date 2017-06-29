#!/usr/bin/env python

import requests
import mwparserfromhell as mwparser
import re
import lxml.etree as ET

vsh_url = 'http://www.psdevwiki.com/ps3/index.php?title=VSH_Exports&action=raw'



def clean(s):
	# Remove invalid characters
	s = re.sub('[^0-9a-zA-Z_]', '', s)

	# Remove leading characters until we find a letter or underscore
	s = re.sub('^[^a-zA-Z_]+', '', s)

	return s

#r = requests.get(vsh_url)
#raw = r.text

f = open('vsh.wiki')
raw = f.read()
f.close()

wc = mwparser.parse(raw)

groups = {}

for sec in wc.get_sections():
	headings = sec.filter_headings()
	if len(headings) != 1:
		continue
	heading = headings[0]
	group = heading.split(' ')[1]
	groups[group] = {}
	idx = sec.index(heading)
	#print sec
	table = sec.filter_tags(matches=lambda node: node.tag == "table")[0]
	#print table
	cont = table.contents.split('\n')
	for row in cont:
		if not row.startswith('| '):
			continue
		row = row[2:]
		cols = row.split('||')
		nid = cols[0].strip()
		symbol = cols[1].strip()
		groups[group][nid] = clean(symbol)


db = ET.Element("IdaInfoDatabase")
for lib, syms in groups.iteritems():
	group = ET.SubElement(db, "Group", name=lib)
	for nid, symbol in syms.iteritems():
		ET.SubElement(group, "Entry", id=nid, name=symbol)

tree = ET.ElementTree(db)
xml = ET.tostring(tree, pretty_print = True)
f = open('ps3.xml', 'w')
f.write(xml)
f.close()
