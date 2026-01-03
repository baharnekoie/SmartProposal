

def analyze_text(text, use_knowledge=False):
    base_analysis = f"Analysis: {text}"

    if use_knowledge:
        knowledge = " | Extra knowledge applied"
        return base_analysis + knowledge

    return base_analysis
