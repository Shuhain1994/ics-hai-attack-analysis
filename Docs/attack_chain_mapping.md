# Attack Chain Mapping – HAI ICS Dataset (Process-Aware Perspective)

This document provides a **conceptual attack chain mapping** for the attack scenarios analyzed in this project.  
The mapping focuses on **attacker intent and technique categories**, rather than claiming successful detection or confirmation of impact.

The purpose of this document is to bridge **process-level observations** with **ICS security frameworks**, enabling clearer communication with SOC and OT security stakeholders.

---

## 1. Scope and Methodology

This attack chain mapping:

- Is based on **observable process data only** (SP, PV, CV)
- Does **not** assume access to network traffic, PLC logic, or attacker tooling
- Maps **attack intent and technique**, not detection success
- Uses terminology aligned with **MITRE ATT&CK for ICS**, at a conceptual level

The mapping intentionally avoids over-specification to prevent unsupported claims.

---

## 2. SA08 – Attack Chain Mapping

### 2.1 Scenario Summary

SA08 targets the **P1-LC level control loop** through manipulation of the controller setpoint and replay of sensor values.  
The apparent objective is to influence control behavior while minimizing visibility to operators and basic monitoring mechanisms.

---

### 2.2 Attack Objective

- Influence physical process behavior
- Maintain plausibility of operator-facing signals
- Avoid triggering simple threshold-based alarms

---

### 2.3 Conceptual Attack Techniques (ICS Context)

| Layer | Technique Description |
|-----|----------------------|
| Control Layer | Manipulation of control setpoints |
| Sensor Layer | Replay or masking of sensor feedback |
| Operator Layer | Reduction of operator situational awareness |

These techniques align with the general category of **Manipulation of Control** in ICS-focused threat models.

---

### 2.4 Observable Effects

- Setpoint (SP) changes remain within plausible operational bounds
- Process Variable (PV) appears consistent with expected behavior
- Control Variable (CV) adjusts normally in response to SP–PV relationships

---

### 2.5 Detection Challenges

- No single-variable anomaly is sufficient for reliable detection
- Process-level signals alone cannot confirm malicious intent
- Early-stage or stealthy execution minimizes observable deviation

This scenario illustrates how **successful attack execution does not guarantee detectable process anomalies**.

---

## 3. MA06 – Composed Attack Chain Mapping (SA08 + SA14)

### 3.1 Scenario Structure

MA06 is a **composed attack scenario**, consisting of two coordinated components:

- **SA08** – Setpoint manipulation and sensor replay
- **SA14** – Additional malicious influence affecting the same control loop

The attack unfolds across multiple stages rather than a single isolated action.

---

### 3.2 Attack Objective

- Gradually influence control behavior over time
- Distribute malicious actions to reduce per-stage detectability
- Exploit the lack of cross-stage correlation in simple monitoring setups

---

### 3.3 Multi-Stage Attack Chain (Conceptual)

| Stage | Action | Security Interpretation |
|-----|-------|------------------------|
| Stage 1 (SA08) | SP manipulation + feedback masking | Subtle control influence |
| Stage 2 (SA14) | Additional control interference | Reinforcement of long-term effect |

Each stage may appear benign in isolation, but collectively contributes to the attacker’s objective.

---

### 3.4 Observable Effects

- Process behavior remains operationally plausible
- No single stage produces definitive anomalies
- Effects are distributed across time and variables

This structure highlights the difficulty of detecting **composed attacks** using surface-level process monitoring.

---

### 3.5 Detection Implications

- Single-stage analysis may fail to identify malicious intent
- Correlation across stages is required
- Additional visibility (controller internals, network activity) would significantly improve detection confidence

---

## 4. Relevance to Industrial SOC Operations

From an SOC perspective, these mappings demonstrate that:

- Attack labels represent **intent**, not guaranteed detection
- Absence of alerts does not imply absence of adversarial activity
- Escalation decisions often require contextual enrichment beyond process data

The scenarios analyzed here are representative of **low-and-slow or stealth-oriented ICS attacks**.

---

## 5. Limitations of the Mapping

This attack chain mapping is constrained by:

- Lack of network telemetry
- Absence of PLC logic or parameter access
- No confirmation of attacker success criteria

As a result, the mapping remains **conceptual and intent-focused**, rather than forensic.

---

## 6. Summary

This document complements the process-level analysis by providing a structured security interpretation of SA08 and MA06.

By mapping attack intent without overstating detection success, the analysis remains technically accurate, reproducible, and aligned with real-world ICS security practices.
