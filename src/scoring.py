def compute_scores(engine, jd_text, docs, required_skills=[], min_years=0):
    scores = []

    for doc in docs:
        similarity = engine.compute_similarity(jd_text, doc)
        matched_skills = [s for s in required_skills if s.lower() in doc.lower()]
        matched_count = len(matched_skills)
        years = min_years  # Replace with actual extraction if available

        final_score = similarity + 0.1 * matched_count

        justification = f"sim={similarity:.3f} | skills={matched_count}/{len(required_skills)} | years={years}"

        scores.append({
            "final_score": final_score,
            "similarity": similarity,
            "matched_skills": matched_skills,
            "matched_skill_list": matched_skills,
            "years": years,
            "justification": justification,
            "raw": doc
        })

    return scores
