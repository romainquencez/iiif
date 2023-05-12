from iiif.static import IIIFStatic
import sys

def main():
    sg = IIIFStatic(dst="dist")
    sg.generate(sys.argv[1])
    sg.write_html(include_osd=True)

main()
