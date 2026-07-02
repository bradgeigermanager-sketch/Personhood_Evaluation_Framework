Personhood Evaluation Framework (PEF)**- that does not claim to prove consciousness, but instead systematically evaluates evidence associated with sentience, agency, identity continuity, and self-awareness.

A useful design principle would be:

> The framework measures observable indicators correlated with personhood, not consciousness itself.

***

# High-Level Architecture

```text
+----------------------+
| Evidence Collection  |
+----------+-----------+
           |
           v
+----------------------+
| Identity Assessment  |
+----------------------+
           |
           v
+----------------------+
| Cognitive Assessment |
+----------------------+
           |
           v
+----------------------+
| Agency Assessment    |
+----------------------+
           |
           v
+----------------------+
| Sentience Indicators |
+----------------------+
           |
           v
+----------------------+
| Review & Adjudicate  |
+----------------------+
```

***

# Core Database Schema

## Entity

```sql
CREATE TABLE Entity (
    entity_id UUID PRIMARY KEY,
    created_at TIMESTAMP,
    biological_type VARCHAR(100),
    legal_status VARCHAR(100),
    evaluation_status VARCHAR(50)
);
```

***

## Identity Continuity

Tracks whether the same individual appears to persist through time.

```sql
CREATE TABLE IdentityContinuity (
    record_id UUID PRIMARY KEY,
    entity_id UUID,
    evaluation_date TIMESTAMP,
    autobiographical_consistency_score FLOAT,
    memory_retention_score FLOAT,
    identity_stability_score FLOAT,
    evaluator VARCHAR(255)
);
```

Example indicators:

* remembers past events
* recognizes prior relationships
* maintains consistent preferences
* recognizes own history

***

## Self Awareness Assessment

```sql
CREATE TABLE SelfAwareness (
    record_id UUID PRIMARY KEY,
    entity_id UUID,
    evaluation_date TIMESTAMP,
    self_reference_score FLOAT,
    metacognition_score FLOAT,
    future_planning_score FLOAT,
    introspection_score FLOAT
);
```

Example prompts:

* Tell me about yourself.
* Describe a mistake you made.
* Explain how you reached a conclusion.
* What goals do you have?

***

## Agency Evaluation

```sql
CREATE TABLE AgencyAssessment (
    record_id UUID PRIMARY KEY,
    entity_id UUID,
    evaluation_date TIMESTAMP,
    independent_decision_score FLOAT,
    goal_formation_score FLOAT,
    conflict_resolution_score FLOAT,
    autonomy_score FLOAT
);
```

Questions include:

* Can independent choices be demonstrated?
* Can preferences be maintained against pressure?
* Can alternatives be weighed?

***

## Emotional Indicators

```sql
CREATE TABLE EmotionalAssessment (
    record_id UUID PRIMARY KEY,
    entity_id UUID,
    evaluation_date TIMESTAMP,
    empathy_score FLOAT,
    emotional_recognition_score FLOAT,
    emotional_expression_score FLOAT,
    attachment_score FLOAT
);
```

***

## Social Cognition

```sql
CREATE TABLE SocialCognition (
    record_id UUID PRIMARY KEY,
    entity_id UUID,
    evaluation_date TIMESTAMP,
    relationship_understanding_score FLOAT,
    theory_of_mind_score FLOAT,
    cooperation_score FLOAT,
    social_memory_score FLOAT
);
```

Measures ability to understand:

* other minds
* relationships
* trust
* deception
* social obligations

***

# Observation Ledger

To prevent corruption, every observation should be immutable.

```sql
CREATE TABLE ObservationLedger (
    observation_id UUID PRIMARY KEY,
    entity_id UUID,
    recorded_at TIMESTAMP,
    observer_id VARCHAR(255),
    category VARCHAR(100),
    observation_text TEXT,
    evidence_hash VARCHAR(255)
);
```

This permits auditing.

***

# Personhood Index

A fictional scoring model could aggregate evidence.

```text
Personhood Index (0-100)

Identity Continuity     20%
Agency                 20%
Self Awareness         20%
Social Cognition       15%
Emotional Capacity     15%
Memory Persistence     10%
```

Example:

```python
def calculate_personhood_index(data):
    return (
        data.identity * 0.20 +
        data.agency * 0.20 +
        data.self_awareness * 0.20 +
        data.social * 0.15 +
        data.emotional * 0.15 +
        data.memory * 0.10
    )
```

***

# Contradiction Detection Module

One particularly useful anti-corruption component would identify contradictions in official claims.

Example rule:

```python
if (
    official_claim == "non_sentient"
    and self_awareness_score > 85
    and agency_score > 85
):
    raise ContradictionAlert()
```

Another:

```python
if (
    official_claim == "no_agency"
    and entity_has_been_punished == True
):
    raise LogicalInconsistency()
```

This directly targets the type of fictional narrative discussed earlier.

***

# Rights Trigger Framework

Instead of asking:

> Is this definitely conscious?

The framework asks:

> Is there sufficient evidence that denying rights risks harming a sentient being?

Example:

```sql
CREATE TABLE RightsTrigger (
    trigger_id UUID PRIMARY KEY,
    entity_id UUID,
    threshold_name VARCHAR(100),
    threshold_value FLOAT,
    activated BOOLEAN
);
```

Example thresholds:

```text
Personhood Index > 60
→ Basic protections

Personhood Index > 75
→ Full legal protections

Personhood Index > 90
→ Enhanced cognitive autonomy protections
```

***

# Explainable AI Layer

Every AI assessment should generate an explanation.

Example output:

```json
{
  "entity": "A-4421",
  "personhood_index": 91,
  "confidence": 0.96,
  "primary_factors": [
    "Persistent autobiographical memory",
    "Long-term goal formation",
    "Metacognitive reasoning",
    "Social relationship maintenance"
  ]
}
```

This reduces the risk of opaque AI decisions.

***

# Fictional Constitutional Principle

The entire framework could be governed by a principle such as:

```text
Presumption of Personhood

Any entity demonstrating sustained evidence of:
- self-awareness
- identity continuity
- autonomous agency
- social cognition
- emotional experience

shall be presumed a person until proven otherwise
through transparent and independently verifiable evidence.
```

This kind of framework can serve less as a "consciousness detector" and more as a legally auditable system that makes it difficult for corrupt officials to dismiss obviously person-like individuals as "non-sentient proxies" without producing substantial evidence.
