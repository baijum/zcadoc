rm -fr zca.*
rst2html --stylesheet=zope3.css izca.txt > zca.html 
rst2latex --use-latex-toc --stylesheet=style.tex --documentclass=book --use-latex-footnotes izca.txt > zca.tex
pdflatex zca.tex
pdflatex zca.tex
