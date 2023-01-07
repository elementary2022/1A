
$$
\documentclass{article}

\usepackage{xeCJK}
\setCJKmainfont{KaiTi}

\usepackage{tikz}

% \grid for a single character
\newcommand\grid[1]{%
\begin{tikzpicture}[baseline=(char.base)]
  \path[use as bounding box]
    (0,0) rectangle (1em,1em);
  \draw[help lines,step=0.5em]
    (0,0) grid (1em,1em);
  \draw[help lines,dashed]
    (0,0) -- (1em,1em)  (0,1em) -- (1em,0);
  \node[inner sep=0pt,anchor=base west]
    (char) at (0em,\gridraiseamount) {#1};
\end{tikzpicture}}

% \gridraiseamount is a font-specific value
\newcommand\gridraiseamount{0.12em}

% \Grid for a CJK string
\makeatletter
\newcommand\Grid[1]{%
  \@tfor\z:=#1\do{\grid{\z}}}
\makeatother

\begin{document}

\Huge
\xeCJKsetup{PunctStyle=plain}

明月出天山，苍茫云海间。

\Grid{明月出天山，苍茫云海间。}

% We use a dash to test \gridraiseamount
\grid{—}

\end{document}
$$