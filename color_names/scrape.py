import requests
from pyquery import PyQuery as pq
from colour import Color

URL_W3 = "https://www.w3.org/TR/css3-color/#svg-color"
SELECTOR_W3 = ".colortable:last tbody td, .colortable:last dfn"  # wat
LEGAL_W3 = """ORIGINAL URL: https://www.w3.org/TR/css3-color/#html4
COPYRIGHT: Copyright © 2011 World Wide Web Consortium, (MIT, ERCIM, Keio, Beihang). http://www.w3.org/Consortium/Legal/2015/doc-license
STATUS: This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the W3C technical reports index at http://www.w3.org/TR/.

The (archived) public mailing list www-style@w3.org (see instructions) is preferred for discussion of this specification. When sending e-mail, please put the text “css3-color” in the subject, preferably like this: “[css3-color] …summary of comment…”

This document was produced by the CSS Working Group (part of the Style Activity).

A separate implementation report contains a test suite and shows that each test in the test suite was passed by at least two independent implementations.

The list of comments on the most recent Last Call draft explains the changes that were made since that draft. Comments received during the Candidate Recommendation period (for the 14 May 2003 draft) and how they were addressed in this draft can be found in the disposition of comments. Comments received during the Last Call period (for the 14 February 2003 draft) and how they were addressed can be found in the disposition of comments.

A complete list of changes to this document is available.

This document has been reviewed by W3C Members, by software developers, and by other W3C groups and interested parties, and is endorsed by the Director as a W3C Recommendation. It is a stable document and may be used as reference material or cited from another document. W3C's role in making the Recommendation is to draw attention to the specification and to promote its widespread deployment. This enhances the functionality and interoperability of the Web.

This document was produced by a group operating under the 5 February 2004 W3C Patent Policy. W3C maintains a public list of any patent disclosures made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains Essential Claim(s) must disclose the information in accordance with section 6 of the W3C Patent Policy.
"""

URL_RESENE = "http://people.csail.mit.edu/jaffer/Color/resenecolours.txt"
LEGAL_RESENE = """Resene RGB Values List
For further information refer to http://www.resene.co.nz
Copyright Resene Paints Ltd 2001

Permission to copy this software, to modify it, to redistribute it,
to distribute modified versions, and to use it for any purpose is
granted, subject to the following restrictions and understandings.

1. Any text copy made of this dictionary must include this copyright
notice in full.

2. Any redistribution in binary form must reproduce this copyright
notice in the documentation or other materials provided with the
distribution.

3. Resene Paints Ltd makes no warranty or representation that this
dictionary is error-free, and is under no obligation to provide
any services, by way of maintenance, update, or otherwise.

4. There shall be no use of the name of Resene or Resene Paints Ltd in
any advertising, promotional, or sales literature without prior
written consent in each case.

5. These RGB colour formulations may not be used to the detriment of
Resene Paints Ltd."""

URL_WIKI = "https://en.wikipedia.org/wiki/List_of_colors_%28compact%29"
URL_CRAYOLA = "https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors"


def fetch_w3():
    raw_w3 = pq(URL_W3)(SELECTOR_W3)
    data_w3 = [r.text.strip() for r in raw_w3 if (r.text and r.text.strip())]
    return zip(data_w3[0::3], (Color(_) for _ in data_w3[1::3])), LEGAL_W3


def fetch_resene():
    raw_resene = (r.decode().split('\t')
                  for r in requests.get(URL_RESENE).content.splitlines()[27:])
    data_resene = ((' '.join(n.split()[1:])[:-1],
                    Color('#' + hex(int(r) * 0x10000 +
                                    int(g) * 0x100 +
                                    int(b))[2:].zfill(6)))
                   for (n, r, g, b) in raw_resene)
    return data_resene, LEGAL_RESENE

if __name__ == "__main__":
    print(list(fetch_w3())[0])
    print(list(fetch_resene())[0])
