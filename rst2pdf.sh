rm -fr zca.*

# English
rst2html.py --stylesheet=zope3.css izca.txt > zca.html 
rst2latex.py --use-latex-docinfo --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes izca.txt > zca.tex
pdflatex zca.tex
pdflatex zca.tex

# Spanish translation
rst2html.py --stylesheet=zope3.css izca-es.txt > zca-es.html 
rst2latex.py --use-latex-docinfo --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes izca-es.txt > zca-es.tex
pdflatex zca-es.tex
pdflatex zca-es.tex

# French translation
rst2html.py --stylesheet=zope3.css izca-fr.txt > zca-fr.html 
rst2latex.py --use-latex-docinfo --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes izca-fr.txt > zca-fr.tex
pdflatex zca-fr.tex
pdflatex zca-fr.tex

# Russian translation
rst2html.py --stylesheet=zope3.css izca-ru.txt > zca-ru.html 
rst2latex.py --use-latex-docinfo --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes --output-encoding=utf8 --documentoptions=10pt,a4paper,russian,english --font-encoding=T2A izca-ru.txt > zca-ru.tex
pdflatex zca-ru.tex
pdflatex zca-ru.tex
