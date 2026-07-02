from dataclasses import dataclass


@dataclass
class IdentityEvidence:
    memory_retention_score: float
    autobiographical_consistency_score: float
    preference_stability_score: float
    relationship_recognition_score: float
    self_narrative_consistency_score: float


class IdentityContinuityEngine:

    WEIGHTS = {
        "memory_retention": 0.25,
        "autobiographical_consistency": 0.25,
        "preference_stability": 0.15,
        "relationship_recognition": 0.15,
        "self_narrative_consistency": 0.20
    }

    def calculate_score(self, evidence: IdentityEvidence) -> float:

        score = (
            evidence.memory_retention_score *
            self.WEIGHTS["memory_retention"] +

            evidence.autobiographical_consistency_score *
            self.WEIGHTS["autobiographical_consistency"] +

            evidence.preference_stability_score *
            self.WEIGHTS["preference_stability"] +

            evidence.relationship_recognition_score *
            self.WEIGHTS["relationship_recognition"] +

            evidence.self_narrative_consistency_score *
            self.WEIGHTS["self_narrative_consistency"]
        )

        return round(score, 2)

    def continuity_level(self, score: float) -> str:

        if score >= 90:
            return "Very High Continuity"

        if score >= 75:
            return "High Continuity"

        if score >= 60:
            return "Moderate Continuity"

        if score >= 40:
            return "Low Continuity"

        return "Insufficient Evidence"


# Example

evidence = IdentityEvidence(
    memory_retention_score=92,
    autobiographical_consistency_score=88,
    preference_stability_score=85,
    relationship_recognition_score=91,
    self_narrative_consistency_score=89
)

engine = IdentityContinuityEngine()

score = engine.calculate_score(evidence)

result = {
    "identity_continuity_score": score,
    "assessment": engine.continuity_level(score)
}

print(result)
