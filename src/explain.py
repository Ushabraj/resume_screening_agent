def highlight_matches(text, skills):
    """
    Returns HTML where matched skills are highlighted in yellow
    """
    for skill in skills:
        text = text.replace(skill, f"<mark>{skill}</mark>")
        text = text.replace(skill.lower(), f"<mark>{skill.lower()}</mark>")
        text = text.replace(skill.upper(), f"<mark>{skill.upper()}</mark>")
    return text
