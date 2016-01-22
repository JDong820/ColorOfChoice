#color-names
*in development*


A python module to translate colors and names.

## Description
`color_names` provides translations between color codes and color names.
[Many formats](#supported-color-formats) are supported for color description.
Additionally, [multiple dictionaries](#included-color-dictionaries) are
included for color names with the option of passing in user-defined
dictionaries. 

### Supported Color Formats
Supported color formats are: 
* RGB Color Format
* 6-digit and 3-digit hex
* HSL Color Format
<!---
* CMY(K) Color Format
* YUV Color Format
* YCbCr Color Format
* YPbPr Color Format
-->
These formats are the formats supported by the python
[colour](https://github.com/vaab/colour) module.

### Included Color Dictionaries
* Wikipedia-based dictionary (default)
* Pantone® PMS
* Resene
* W3 CSS3
* X11
* Crayola
* Python matplotlib

Also see the [sources](#color-dictionary-sources) for more information on
color names.

## Color Dictionary Sources

### Links
* [Pantone® PMS Used for Printing Labels](http://cal-print.com/InkColorChart.htm)
* [Resene](http://people.csail.mit.edu/jaffer/Color/resenecolours.txt)
* [Wikipedia](https://en.wikipedia.org/wiki/List_of_colors_%28compact%29)
* [W3 CSS3](https://www.w3.org/TR/css3-color/#svg-color)
* [Crayola](https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors)

### Notes
[X11 colors](https://en.wikipedia.org/wiki/X11_color_names) have been aliased
to the W3 colors as X11 colors are not a fixed specification.
Additionally, W3 includes gray/grey variants.
