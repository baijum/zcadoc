rm -fr zca.*

# English
rst2html --stylesheet=zope3.css izca.txt > zca.html 
rst2latex --use-latex-docinfo --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes izca.txt > zca.tex
pdflatex zca.tex
pdflatex zca.tex

# Spanish translation
rst2html --stylesheet=zope3.css izca-es.txt > zca-es.html 
rst2latex --use-latex-docinfo --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes izca-es.txt > zca-es.tex
pdflatex zca-es.tex
pdflatex zca-es.tex

# French translation
rst2html --stylesheet=zope3.css izca-fr.txt > zca-fr.html 
rst2latex --use-latex-docinfo --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes izca-fr.txt > zca-fr.tex
pdflatex zca-fr.tex
pdflatex zca-fr.tex
