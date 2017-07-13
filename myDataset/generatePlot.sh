#!/bin/sh

bn=`basename $1 .gp`
gnuplot $bn.gp
epstopdf $bn.ps
pdfcrop $bn.pdf
mv $bn-crop.pdf $bn.pdf
rm $bn.ps