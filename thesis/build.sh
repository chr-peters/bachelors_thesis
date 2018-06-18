#! /bin/sh

MAIN_FILE="bachelorthesis_christian_peters"

# set and create output directory
OUTPUT_DIR=latex_output
mkdir -p $OUTPUT_DIR

# compile twice when successful once
pdflatex -output-directory="$OUTPUT_DIR" "$MAIN_FILE.tex" && pdflatex -output-directory="$OUTPUT_DIR" "$MAIN_FILE.tex"

# run biber
biber "$OUTPUT_DIR/$MAIN_FILE"

# recompile
if pdflatex -output-directory="$OUTPUT_DIR" "$MAIN_FILE.tex"
then
    # move .pdf to main directory
    mv "$OUTPUT_DIR/$MAIN_FILE.pdf" .
fi

