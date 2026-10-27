# Rule-Based Expert System (Forward Chaining)

A modular, lightweight Rule-Based Expert System built in Python for **Syntecxhub Internship Task 1 (Project 2)**.

## Project Features
- **Fact & Rule Base Modeling:** Defines rules structured with antecedents (IF condition) and consequents (THEN conclusion).
- **Forward Chaining Inference:** Multi-step deduction engine that continues deriving new facts until no further rules apply.
- **Reasoning Log:** Step-by-step transparency logging showing exactly which rules were triggered and why.
- **Interactive CLI:** Easy-to-use user interface for entering custom facts and inspecting derived results.

## Requirements
- Python 3.x (No third-party packages required).

## How to Run
1. Clone repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Syntecxhub_Rule_Based_Expert_System.git
   cd Syntecxhub_Rule_Based_Expert_System
   ```
2. Execute script:
   ```bash
   python main.py
   ```

## Example Usage
**User Input:** `fever, cough, fatigue`

**Inference Logs:**
```text
--- Starting Inference Engine (Forward Chaining) ---
Initial Facts: ['cough', 'fatigue', 'fever']
Step 1: Rule [Detect Respiratory Infection] triggered! IF ['cough', 'fever'] THEN derived 'respiratory_infection'
Step 2: Rule [Diagnose Flu] triggered! IF ['fatigue', 'respiratory_infection'] THEN derived 'flu'
Step 3: Rule [Treatment Recommendation] triggered! IF ['flu'] THEN derived 'recommend_rest_and_fluids'
--- Inference Completed: No further rules can fire ---
```