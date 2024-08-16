from .models import Recipe


def recipe_to_latex(recipe: Recipe) -> str:
    title = recipe.title
    description = recipe.description
    ingredient_groups = recipe.ingredient_groups
    instruction_groups = recipe.instruction_groups
    # reviews = recipe.reviews
    # meta = recipe.meta
    # rating = recipe.rating

    # source_latex = "\\fancyfoot[C]{\\footnotesize " + _escape_latex(source) + "}" if source else ""

    latex = [
        "\\documentclass[10pt]{article}",
        "\\pdfvariable suppressoptionalinfo \\numexpr32+64+512\\relax",
        "\\usepackage{fontspec}",
        "\\usepackage{geometry}",
        "\\usepackage{enumitem}",
        "\\usepackage{graphicx}",
        "\\usepackage{paracol}",
        "\\usepackage{microtype}",
        "\\usepackage{parskip}",
        "\\usepackage{fancyhdr}",
        "\\geometry{letterpaper, margin=0.75in}",
        "\\setmainfont{TeX Gyre Termes}",
        "\\newfontfamily\\headingfont{TeX Gyre Termes}",
        "\\pagestyle{fancy}",
        "\\fancyhf{}",
        "\\renewcommand{\\headrulewidth}{0pt}",
        # source_latex,
        "\\begin{document}",
        "\\setlist[enumerate,1]{itemsep=0em}",
        "\\begin{center}",
        "{\\huge \\bfseries \\headingfont " + _escape_latex(title) + "}",
        "\\end{center}",
        "\\vspace{1em}"
    ]

    if description:
        latex.append("\\noindent " + _escape_latex(description))

    # if meta:
    #     latex.append("\\begin{center}")
    #     if meta.prep_time_minutes:
    #         latex.append(f"Prep Time: {meta.prep_time_minutes} min | ")
    #     if meta.cook_time_minutes:
    #         latex.append(f"Cook Time: {meta.cook_time_minutes} min | ")
    #     if meta.total_time_minutes:
    #         latex.append(f"Total Time: {meta.total_time_minutes} min | ")
    #     if meta.recipe_yield:
    #         latex.append(f"Yield: {_escape_latex(meta.recipe_yield)}")
    #     latex.append("\\end{center}")
    #
    # if rating and rating.value:
    #     latex.append("\\begin{center}")
    #     latex.append(f"Rating: {rating.value:.1f}/5 ({rating.count} reviews)")
    #     latex.append("\\end{center}")

    latex.append("\\vspace{1em}")
    latex.append("\\columnratio{0.35}")
    latex.append("\\begin{paracol}{2}")
    latex.append("\\section*{Ingredients}")
    latex.append("\\raggedright")

    for ingredient_group in ingredient_groups:
        if ingredient_group.name:
            latex.append(f"\\subsection*{{{_escape_latex(ingredient_group.name)}}}")
        latex.append("\\begin{itemize}[leftmargin=*]")
        for ingredient in ingredient_group.ingredients:
            latex.append(f"\\item {_escape_latex(ingredient)}")
        latex.append("\\end{itemize}")

    latex.append("\\switchcolumn")
    latex.append("\\section*{Instructions}")

    for instruction_group in instruction_groups:
        if instruction_group.name:
            latex.append(f"\\subsection*{{{_escape_latex(instruction_group.name)}}}")
        latex.append("\\begin{enumerate}[leftmargin=*]")
        for instruction in instruction_group.instructions:
            latex.append(f"\\item {_escape_latex(instruction)}")
        latex.append("\\end{enumerate}")

    latex.append("\\end{paracol}")

    # if reviews:
    #     latex.append("\\section*{Reviews}")
    #     for review in reviews:
    #         if review.author:
    #             latex.append(f"\\textbf{{{_escape_latex(review.author)}}}")
    #         if review.rating:
    #             latex.append(f" - Rating: {review.rating:.1f}/5")
    #         latex.append("\\\\")
    #         if review.body:
    #             latex.append(_escape_latex(review.body))
    #         latex.append("\\par\\vspace{0.5em}")

    latex.append("\\end{document}")
    latex.append("")

    return "\n".join(latex)


def _escape_latex(text: str) -> str:
    mapping = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}'
    }
    return "".join(mapping.get(c, c) for c in text)
