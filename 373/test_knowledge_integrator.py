# test_knowledge_integrator.py

import pytest
from knowledge_integrator import analyze_text


def test_analysis_with_and_without_knowledge():
    documents = [
        "Patient has fever",
        "Loan application was rejected",
        "Student failed the exam"
    ]

    for doc in documents:
        output_without_knowledge = analyze_text(doc, use_knowledge=False)
        output_with_knowledge = analyze_text(doc, use_knowledge=True)

        # bayad khoroojiha fargh dashte bashand
        assert output_without_knowledge != output_with_knowledge

        # khorooji ba knowledge bayad etelaate bishtari dashte bashad
        assert len(output_with_knowledge) > len(output_without_knowledge)
