#!/usr/bin/env bash
_group=8
if [ "${#}" -gt 0 ]; then
    _group="${1}"
fi
_pwd=$(pwd)
_locate=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)

pushd "${_locate}"

problem="${_pwd}/.problem.tex.block"
reference="${_pwd}/.reference.tex.block"
python3 ./simple_addition.py "${_group}" "${problem}" "${reference}"

_problem_tex="${_pwd}/problem.tex"
echo '\documentclass{article}' > "${_problem_tex}"
echo '\usepackage{amsmath}' >> "${_problem_tex}"
echo '\pagenumbering{gobble}' >> "${_problem_tex}"
echo '\begin{document}' >> "${_problem_tex}"
echo '\begin{sloppy}' >> "${_problem_tex}"
echo '\begin{center}' >> "${_problem_tex}"
echo '{\fontfamily{pcr}\selectfont {Started:}\underline{\hspace{1.5cm}}{Finished:}\underline{\hspace{1.5cm}}{Solved:}\underline{\hspace{1.5cm}}}' >> "${_problem_tex}"
echo '\end{center}' >> "${_problem_tex}"
echo '\hrule' >> "${_problem_tex}"
echo '\begin{align*}' >> "${_problem_tex}"
while read -r line; do
    echo "    ${line}" >> "${_problem_tex}"
done < "${problem}"
echo '\end{align*}' >> "${_problem_tex}"
echo '\hrule' >> "${_problem_tex}"
echo '\end{sloppy}' >> "${_problem_tex}"
echo '\end{document}' >> "${_problem_tex}"

_reference_tex="${_pwd}/reference.tex"
echo '\documentclass{article}' > "${_reference_tex}"
echo '\usepackage{amsmath}' >> "${_reference_tex}"
echo '\pagenumbering{gobble}' >> "${_reference_tex}"
echo '\begin{document}' >> "${_reference_tex}"
echo '\begin{sloppy}' >> "${_reference_tex}"
echo '\hrule' >> "${_reference_tex}"
echo '\begin{align*}' >> "${_reference_tex}"
while read -r line; do
    echo "    ${line}" >> "${_reference_tex}"
done < "${reference}"
echo '\end{align*}' >> "${_reference_tex}"
echo '\hrule' >> "${_reference_tex}"
echo '\end{sloppy}' >> "${_reference_tex}"
echo '\end{document}' >> "${_reference_tex}"

popd

pdflatex "${_problem_tex}"
pdflatex "${_reference_tex}"

echo '![visual](problem.jpg)' >> README.md
